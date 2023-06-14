<template>
  <v-container class="text-center">
    <h1>{{ marketName }}</h1>
    <v-row class="justify-center">
      <v-col cols="3" v-for="product in productList" class="ma-3 text-start">
        <v-card>
          <v-card-title>{{ product.product_name }}</v-card-title>
          <v-card-subtitle>{{ product.brand }}</v-card-subtitle>
          <v-card-title>Price: ${{ product.price }}</v-card-title>
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
    </v-row>

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
          v-model="quantity"
          type="number"
          label="數量"
        ></v-text-field>
        <v-card-actions>
          <v-row class="justify-end mx-3">
            <v-btn
              color="blue-darken-1"
              variant="tonal"
              prepend-icon="mdi-cart"
              @click="addCart"
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
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import Product from "../models/product/product";
import ProductDataService from "../services/ProductDataService";
import AddtoCart from "../models/cart/add-to-cart";
import CartDataService from "../services/CartDataService";
import MarketDataService from "../services/MarketDataService";

export default defineComponent({
  setup() {
    const route = useRoute();
    return { route };
  },

  data() {
    return {
      productList: [] as Product[],
      selectedProduct: {} as Product,
      dialog: false,
      quantity: 1,
      marketName: "",
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

    addCart() {
      const user_id = Number(sessionStorage.getItem("user"));
      if (user_id) {
        const data: AddtoCart = {
          member_id: user_id,
          market_id: this.selectedProduct.market_id,
          product_id: this.selectedProduct.product_id,
          quantity: this.quantity,
        };
        CartDataService.addToCart(data)
          .then((response: any) => {
            console.log(response.data);
            this.dialog = false;
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    close() {
      this.dialog = false;
      this.quantity = 1;
    },
  },

  mounted() {
    this.getProductList();
  },
});
</script>
