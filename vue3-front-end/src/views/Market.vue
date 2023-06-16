<template>
  <v-container class="text-center">
    <h1>{{ marketName }}</h1>
    <v-row class="justify-center">
      <template v-for="product in productList">
        <v-col
          cols="3"
          class="ma-3 text-start"
          v-if="product.status == false && product.stock != 0"
        >
          <v-card>
            <v-card-title>{{ product.product_name }}</v-card-title>
            <v-card-subtitle>{{ product.brand }}</v-card-subtitle>
            <v-card-title>價格: NTD$ {{ product.price }}</v-card-title>
            <v-card-actions>
              <v-btn
                rounded="lg"
                variant="tonal"
                color="blue-darken-1"
                @click="detail(product)"
              >
                查看更多
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </template>
    </v-row>

    <v-dialog v-model="alertDialog" max-width="500">
      <v-card>
        <v-card-title> 提示訊息 </v-card-title>
        <v-card-text>
          {{ message }}
        </v-card-text>
        <v-card-actions>
          <v-row class="justify-end">
            <v-btn class="mx-3" variant="tonal" @click="alertDialog = false"
              >關閉</v-btn
            >
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5">{{
          selectedProduct.product_name
        }}</v-card-title>
        <v-card-item> 種類 : {{ selectedProduct.category }} </v-card-item>
        <v-card-item> 品牌 : {{ selectedProduct.brand }} </v-card-item>
        <v-card-item> 價格 : {{ selectedProduct.price }} </v-card-item>
        <v-card-item> 庫存 : {{ selectedProduct.stock }} </v-card-item>
        <v-text-field
          class="ma-5"
          v-model="state.quantity"
          type="number"
          label="數量"
          :error-messages="v$.quantity.$errors.map((e: any) => e.$message)"
          @input="v$.quantity.$touch"
          @blur="v$.quantity.$touch"
        ></v-text-field>
        <v-card-actions>
          <v-row class="justify-end mx-3">
            <v-btn
              color="blue-darken-1"
              variant="tonal"
              prepend-icon="mdi-cart"
              @click="addToCart"
            >
              加入購物車
            </v-btn>
            <v-btn variant="tonal" @click="close">關閉</v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { minValue, required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRoute, useRouter } from "vue-router";
import AddtoCart from "../models/cart/add-to-cart";
import Product from "../models/product/product";
import CartDataService from "../services/CartDataService";
import MarketDataService from "../services/MarketDataService";
import ProductDataService from "../services/ProductDataService";

export default defineComponent({
  setup() {
    const route = useRoute();
    const router = useRouter();

    const state = reactive({
      quantity: 1,
    });

    const rules = computed(() => {
      return {
        quantity: {
          required,
          minValue: minValue(1),
        },
      };
    });

    const v$ = useValidate(rules, state);

    return { route, router, state, v$ };
  },

  data() {
    return {
      productList: [] as Product[],
      selectedProduct: {} as Product,
      dialog: false,
      marketName: "",
      alertDialog: false,
      message: "",
    };
  },

  methods: {
    getProductList() {
      const marketId: number = Number(this.route.query.id);
      MarketDataService.get(marketId)
        .then((response: any) => {
          this.marketName = response.data.market_name;
        })
        .catch((e: Error) => {
          console.log(e);
        });
      ProductDataService.getProductByMarket(marketId)
        .then((response: any) => {
          this.productList = response.data;
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    detail(product: Product) {
      this.selectedProduct = product;
      this.dialog = true;
    },

    addToCart() {
      this.v$.$validate();
      if (!this.v$.$error) {
        if (this.state.quantity > this.selectedProduct.stock) {
          this.message = "不可以超過庫存數量 !";
          this.alertDialog = true;
          return;
        }
        const user_id = Number(sessionStorage.getItem("user"));
        if (user_id) {
          const data: AddtoCart = {
            member_id: user_id,
            market_id: this.selectedProduct.market_id,
            product_id: this.selectedProduct.product_id,
            quantity: this.state.quantity,
          };
          CartDataService.addToCart(data)
            .then((response: any) => {
              console.log(response.data);
              this.dialog = false;
            })
            .catch((e: Error) => {
              console.log(e);
            });
        } else {
          this.router.push("/sign-in");
        }
      }
    },

    close() {
      this.dialog = false;
      this.state.quantity = 1;
    },
  },

  mounted() {
    this.getProductList();
  },
});
</script>
