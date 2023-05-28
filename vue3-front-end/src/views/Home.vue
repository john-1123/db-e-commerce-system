<template>
  <v-container class="text-center">
    <h1>Items</h1>
    <v-row 
      class="justify-center"
      no-gutters v-for="market in data.items" :key="market.id">
      <v-col cols="12" md="12" class="ma-3">
        <v-chip size="large" append-icon="mdi-arrow-right">{{ market.market_name }}</v-chip>
      </v-col>

      <v-col
        cols="12"
        sm="6"
        md="3"
        v-for="product in market.product_list"
        :key="product.id"
        class="ma-3 text-start"
      >
        <v-card>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.description }}</v-card-subtitle>
          <v-card-title>Price: ${{ product.price }}</v-card-title>
          <v-card-actions>
            <v-btn rounded="lg" variant="tonal" prepend-icon="mdi-cart">加入購物車</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { computed, defineComponent, reactive, onMounted } from "vue";

export default defineComponent({
  setup() {
    const data = reactive({
      items: [
        {
          market_id: 1,
          market_name: "MARKET NAME",
          product_list: [
            {
              id: 1,
              name: "Item 1",
              description: "This is item 1",
              price: 100,
            },
            {
              id: 2,
              name: "Item 2",
              description: "This is item 2",
              price: 100,
            },
            {
              id: 3,
              name: "Item 3",
              description: "This is item 3",
              price: 100,
            },
            {
              id: 4,
              name: "Item 4",
              description: "This is item 4",
              price: 100,
            },
            {
              id: 5,
              name: "Item 5",
              description: "This is item 5",
              price: 100,
            },
          ],
        },
        {
          market_id: 2,
          market_name: "MARKET NAME",
          product_list: [
            {
              id: 1,
              name: "Item 1",
              description: "This is item 1",
              price: 100,
            },
            {
              id: 2,
              name: "Item 2",
              description: "This is item 2",
              price: 100,
            },
            {
              id: 3,
              name: "Item 3",
              description: "This is item 3",
              price: 100,
            },
            {
              id: 4,
              name: "Item 4",
              description: "This is item 4",
              price: 500,
            },
          ],
        },
      ],
    });
    return { data };
  },

  data() {
    return {};
  },
});
</script>
