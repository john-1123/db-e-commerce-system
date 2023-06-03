<template>
  <v-container class="text-center">
    <h1>Market Product List</h1>
    <v-row class="justify-center">
      <v-col
        cols="12"
        sm="6"
        md="3"
        v-for="product in productList"
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
import { useRoute } from "vue-router";
import Product from "../models/product/product";
import ProductDataService from "../services/ProductDataService";

export default defineComponent({
  setup() {
    const route = useRoute();
    return { route };
  },

  data() {
    return {
      productList: [] as Product[],
    };
  },

  methods: {
    getProductList() {
      const marketId: number = Number(this.route.query.id);
      ProductDataService.getProductByMarket(marketId)
        .then((response: any) => {
          this.productList = response.data;
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },
  },

  mounted() {
    this.getProductList();
  },
});
</script>
