<template>
  <v-container>
    <h1 class="text-center">Home</h1>
    <v-row
      class="justify-start text-left"
      no-gutters
      v-for="market in getGroupByMarket()"
    >
      <v-col cols="12" class="ma-3">
        <v-chip
          size="x-large"
          append-icon="mdi-arrow-right"
          @click="goMarket(market[0].market_id)"
        >
          {{ getMarketName(market[0].market_id) }}
        </v-chip>
      </v-col>
      <v-col
        cols="3"
        v-for="product in market"
        :key="product.product_id"
        class="ma-3 text-start"
      >
        <template v-if="!product.status">
          <v-card>
            <v-card-title>{{ product.product_name }}</v-card-title>
            <v-card-subtitle>{{ product.brand }}</v-card-subtitle>
            <v-card-title
              >Price: NTD${{
                product.price.toLocaleString("zh-TW")
              }}</v-card-title
            >
            <v-card-actions>
              <v-btn
                rounded="lg"
                variant="tonal"
                color="blue-lighten-1"
                @click="detail(product)"
              >
                查看更多
              </v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-col>
    </v-row>

    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5">Product Detail</v-card-title>
        <v-card-item> 名稱 : {{ selectedProduct.product_name }} </v-card-item>
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
              @click="addCart"
              prepend-icon="mdi-cart"
            >
              加入購物車
            </v-btn>
            <v-btn color="blue-darken" variant="tonal" @click="close">
              Close
            </v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import Product from "../models/product/product";
import ProductDataService from "../services/ProductDataService";
import MarketDataService from "../services/MarketDataService";
import CartDataService from "../services/CartDataService";
import AddtoCart from "../models/cart/add-to-cart";

export default defineComponent({
  setup() {
    const router = useRouter();
    return { router };
  },

  data() {
    return {
      productList: [] as Product[],
      marketMap: new Map<number, string>() as Map<number, string>,
      dialog: false,
      selectedProduct: {} as Product,
      quantity: 1,
    };
  },
  methods: {
    getProductList() {
      ProductDataService.getAll()
        .then((response: any) => {
          this.productList = response.data;
          this.productList.forEach((product: Product) => {
            if (!this.marketMap.has(product.market_id)) {
              MarketDataService.get(product.market_id)
                .then((response: any) => {
                  this.marketMap.set(
                    product.market_id,
                    response.data.market_name
                  );
                })
                .catch((e: Error) => {
                  console.log(e);
                });
            }
          });
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    getGroupByMarket() {
      return this.groupBy(this.productList, "market_id");
    },

    getMarketName(marketId: number) {
      return this.marketMap.get(marketId);
    },

    goMarket(marketId: number) {
      this.router.push({
        path: "/market",
        query: {
          id: marketId,
        },
      });
    },

    groupBy(array: any, key: any) {
      // Return the end result
      return array.reduce((result: any, currentValue: any) => {
        // If an array already present for key, push it to the array. Else create an array and push the object
        (result[currentValue[key]] = result[currentValue[key]] || []).push(
          currentValue
        );
        // Return the current iteration `result` value, this will be taken as next iteration `result` value and accumulate
        return result;
      }, {}); // empty object is the initial value for result object
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
