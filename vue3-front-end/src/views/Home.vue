<template>
  <v-container class="text-center">
    <h1>Home</h1>
    <v-btn @click="addToCart('Product 1')">Pro1 Add to Cart</v-btn>
    <v-btn @click="addToCart('Product 2')">Pro2 Add to Cart</v-btn>
    <v-btn @click="addToCart('Product 3')">Pro3 Add to Cart</v-btn>
    <li v-for="item in dcartItems" :key="item">{{ item }}</li>
  </v-container>
</template>

<script lang="ts">
import Cart from './Cart.vue';
import { ref,provide } from 'vue';


export default {
  components:{
    Cart
  },
  setup() {
    const dcartItems = ref([]);

    const addToCart = (product: string) => {
      dcartItems.value.push(product);
    };

    provide('cartItems', dcartItems);

    return { dcartItems,addToCart };
  }
};
</script>
