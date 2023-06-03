<template>
  <v-container class="text-center">
    <h1>Home</h1>
    <v-row
      class="justify-center"
      no-gutters
      v-for="market in getGroupByMarket()"
    >
      <v-col cols="12" md="12" class="ma-3">
        <v-chip size="large" append-icon="mdi-arrow-right" @click="goMarket(market[0].market_id)">
          {{ getMarketName(market[0].market_id) }}
        </v-chip>
      </v-col>
      <v-col
        cols="12"
        sm="6"
        md="3"
        v-for="product in market"
        :key="product.product_id"
        class="ma-3 text-start"
      >
        <v-card>
          <v-card-title>{{ product.product_name }}</v-card-title>
          <v-card-subtitle>{{ product.brand }}</v-card-subtitle>
          <v-card-title>Price: ${{ product.price }}</v-card-title>
          <v-card-actions>
            <v-btn rounded="lg" variant="tonal" prepend-icon="mdi-cart"
              >加入購物車</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import Product from "../models/product/product";
import ProductDataService from "../services/ProductDataService";
import MarketDataService from "../services/MarketDataService";

export default defineComponent({
  setup() {
    const router = useRouter();
    return { router };
  },

  data() {
    return {
      productList: [] as Product[],
      marketMap: new Map<number, string>() as Map<number, string>,
    };
  },
  methods: {
    getProductList() {
      ProductDataService.getAll()
        .then((response: any) => {
          this.productList = response.data;
          this.productList.forEach((product: Product) => {
            if(!this.marketMap.has(product.market_id)) {
              MarketDataService.get(product.market_id)
              .then((response: any) => {
                this.marketMap.set(product.market_id, response.data.market_name);
              })
              .catch((e: Error) => {
                console.log(e);
              });
            }
          })
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
          id: marketId
        }
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
  },

  mounted() {
    this.getProductList();
  },
});
</script>
