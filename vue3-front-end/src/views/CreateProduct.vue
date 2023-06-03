<template>
  <v-container>
    <v-card elevation="2" tile max-width="500" class="ma-auto">
      <v-card-title>Add Product</v-card-title>
      <v-form class="ma-3">
        <v-text-field
          class="ma-3"
          v-model="state.product_name"
          label="Name*"
          :error-messages="v$.product_name.$errors.map((e: any) => e.$message)"
          @input="v$.product_name.$touch"
          @blur="v$.product_name.$touch"
        ></v-text-field>

        <v-text-field
          class="ma-3"
          v-model="state.category"
          label="Category*"
          :error-messages="v$.category.$errors.map((e: any) => e.$message)"
          @input="v$.category.$touch"
          @blur="v$.category.$touch"
        ></v-text-field>

        <v-text-field
          class="ma-3"
          v-model="state.brand"
          label="Brand*"
          :error-messages="v$.brand.$errors.map((e: any) => e.$message)"
          @input="v$.brand.$touch"
          @blur="v$.brand.$touch"
        ></v-text-field>

        <v-text-field
          class="ma-3"
          v-model="state.price"
          label="Price*"
          :error-messages="v$.price.$errors.map((e: any) => e.$message)"
          @input="v$.price.$touch"
          @blur="v$.price.$touch"
        ></v-text-field>

        <v-text-field
          class="ma-3"
          v-model="state.stock"
          label="Stock*"
          :error-messages="v$.stock.$errors.map((e: any) => e.$message)"
          @input="v$.stock.$touch"
          @blur="v$.stock.$touch"
        ></v-text-field>
        <v-btn class="ma-3" color="blue-lighten-1" @click="saveProduct"
          >Add Product!</v-btn
        >
      </v-form>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";
import { CreateProduct } from "../models/product/create-product";
import MarketDataService from "../services/MarketDataService";
import ProductDataService from "../services/ProductDataService";

export default defineComponent({
  name: "create-product",
  setup() {
    const router = useRouter();

    const state = reactive({
      product_name: "",
      category: "",
      brand: "",
      price: 1,
      stock: 1,
      status: false,
      market_id: 0,
    } as CreateProduct);

    const rules = computed(() => {
      return {
        product_name: { required },
        category: { required },
        brand: { required },
        price: { required },
        stock: { required },
      };
    });

    const v$ = useValidate(rules, state);

    return { state, router, v$ };
  },

  methods: {
    saveProduct() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const userId = Number(sessionStorage.getItem("user"));
        if (userId) {
          MarketDataService.getMarketByUser(userId).then((response: any) => {
            const market_id = response.data.market_id;

            const data: CreateProduct = {
              product_name: this.state.product_name,
              category: this.state.category,
              brand: this.state.brand,
              price: this.state.price,
              stock: this.state.stock,
              status: false,
              market_id: market_id,
            };

            ProductDataService.create(data)
              .then((response) => {
                console.log(response.data);
                this.router.push({ name: "ManageProduct" });
              })
              .catch((e: Error) => {
                console.log(e);
              });
          });
        }
      }
    },
  },
});
</script>
