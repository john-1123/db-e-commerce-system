<template>
  <v-container>
    <h2>Product Detail</h2>
    {{ product.product_name }}
  </v-container>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import Product from "../models/product/product";
import ProductDataService from "../services/ProductDataService";
import AddtoCart from "../models/cart/add-to-cart";
import CartDataService from "../services/CartDataService";

export default defineComponent({
  setup() {
    const route = useRoute();
    return { route };
  },
  data() {
    return {
      product: {} as Product,
    };
  },

  methods: {
    getProduct() {
      const productId: number = Number(this.route.query.id);
      ProductDataService.get(productId)
        .then((response: any) => {
          this.product = response.data;
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    addCart(product: Product) {
      const user_id = Number(sessionStorage.getItem("user"));
      if (user_id) {
        const data: AddtoCart = {
          member_id: user_id,
          market_id: product.market_id,
          product_id: product.product_id,
          quntity: 1,
        };
        CartDataService.addToCart(data)
          .then((response: any) => {
            console.log(response.data);
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },
  },

  mounted() {
    this.getProduct();
  },
});
</script>
