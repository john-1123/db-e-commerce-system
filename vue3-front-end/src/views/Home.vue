<template>
  <v-container class="text-center">
    <h1>Items</h1>
    <v-row no-gutters v-for="market in data.items" :key="market.id">
      <v-col cols="12" md="12">
        <v-chip class="ma-2" size="x-large">{{ market.market_name }}</v-chip>
      </v-col>

      <v-col
        cols="12"
        sm="6"
        md="4"
        v-for="product in market.product_list.slice(0, 3)"
        :key="product.id"
      >
        <v-card>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.description }}</v-card-subtitle>
          <v-card-actions>
            <v-btn>${{ product.price }}</v-btn>
            <v-btn>Action 2</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { computed, defineComponent, reactive, onMounted } from "vue";

export default {
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
};
</script>
