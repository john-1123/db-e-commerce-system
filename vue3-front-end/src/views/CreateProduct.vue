<template>
  <div v-if="!submitted">
    <v-container>
      <v-card elevation="2" tile max-width="500" class="ma-auto">
        <v-card-title>Add Product</v-card-title>
        <v-form class="ma-3">
          <v-text-field
            class="ma-3"
            v-model="product.product_name"
            label="ProductName*"
            :error-messages="v$.product_name.$errors.map((e: any) => e.$message)"
            @input="v$.product_name.$touch"
            @blur="v$.product_name.$touch"
            
          ></v-text-field>

          <v-text-field
            class="ma-3"
            v-model="product.category"
            label="Category*"
            :error-messages="v$.category.$errors.map((e: any) => e.$message)"
            @input="v$.category.$touch"
            @blur="v$.category.$touch"
          ></v-text-field>

          <v-text-field
            class="ma-3"
            v-model="product.brand"
            label="Brand*"
            :error-messages="v$.brand.$errors.map((e: any) => e.$message)"
            @input="v$.brand.$touch"
            @blur="v$.brand.$touch"
          ></v-text-field>

          <v-text-field
            class="ma-3"
            v-model="product.price"
            label="Price*"
            :error-messages="v$.price.$errors.map((e: any) => e.$message)"
            @input="v$.price.$touch"
            @blur="v$.price.$touch"
          ></v-text-field>

          <v-text-field
            class="ma-3"
            v-model="product.stock"
            label="Stock*"
            :error-messages="v$.stock.$errors.map((e: any) => e.$message)"
            @input="v$.stock.$touch"
            @blur="v$.stock.$touch"
          ></v-text-field>
          <v-btn @click="saveProduct">Add Product!</v-btn>
        </v-form>
      </v-card>
    </v-container>
  </div>
  <div v-else>
    <h4>You submitted successfully!</h4>
    <button @click="newProduct">Add</button>
  </div>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";
import CreateProduct from "../models/user/product";
import ProductDataService from "../services/ProductDataService";
import Product from "../models/user/product";

export default defineComponent({
  name: "create-product",
  setup() {
    const router = useRouter();
    const product = reactive({
      product_name: "",
      category: "",
      brand: "",
      price: 1,
      stock: 1,
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
    const v$ = useValidate(rules, product);



    return { product, router, v$ };
  },
  data() {
    return {
      submitted: false,
    };
  },

  methods: {
    // saveProduct() {
    //   this.router.push({ name: "ManageProduct" });
    // },
    saveProduct(){
        this.v$.$validate();

        if( !this.v$.$error){
            let data={
                product_name: this.product.product_name,
                category: this.product.category,
                brand: this.product.brand,
                price: this.product.price,
                stock: this.product.stock,
            };
            // const data: CreateProduct = {
            //     product_name: this.product.product_name,
            //     category: this.product.category,
            //     brand: this.product.brand,
            //     price: this.product.price,
            //     stock: this.product.stock
            // };

            ProductDataService.create(data)
                .then((response) => {
                    this.product.product_id = response.data.product_id;
                    console.log(response.data);
                    this.submitted = true;
                    this.router.push({ name: 'ManageProduct' });
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        } 


    },

    newProduct() {
      this.submitted = false;
      this.product = {} as Product;
    },
  },
});
</script>
