<template>
  <v-container class="text-center">
    <h1>Market Product List</h1>
    <v-row>
      <v-col
        cols="12"
        sm="6"
        md="3"
        v-for="product in data.products"
        :key="product.id"
      >
        <v-card>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.description }}</v-card-subtitle>
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
import axios from "axios";
import { computed, defineComponent, reactive, onMounted } from "vue";

export default defineComponent({
  setup() {
    const data = reactive({
      products: [
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
    });
    return { data };
  },

  data() {
    return {};
  },
});
</script>
