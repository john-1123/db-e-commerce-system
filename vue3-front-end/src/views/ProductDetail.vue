<template>
  <div>
    <v-container>
      <h2>/Product Detail/</h2>
      <v-card class="mx-auto" max-width="1000" variant="outlined">
        <v-card-item>
          <div>
            <v-list>
              <v-list-item class="list-item-spacing">
                <div class="text-body-2 font-weight-bold">[Product Name]</div>
                <div class="text-h6 mb-1">{{ productList[2].product_name }}</div>
              </v-list-item>
              <v-spacer></v-spacer>
              <v-list-item class="list-item-spacing">
                <div class="text-body-2 font-weight-bold">[Category]</div>
                <div class="text-h6 mb-1">{{ productList[2].category }}</div>
              </v-list-item>
              <v-list-item class="list-item-spacing">
                <div class="text-body-2 font-weight-bold">[Brand]</div>
                <div class="text-h6 mb-1">{{ productList[2].brand }}</div>
              </v-list-item>
              <v-list-item class="list-item-spacing">
                <div class="text-body-2 font-weight-bold">[Price]</div>
                <div class="text-h6 mb-1">
                  NTD$ {{ productList[2].price.toLocaleString("zh-TW") }}
                </div>
              </v-list-item>
            </v-list>
          </div>
        </v-card-item>
        <!-- <v-card-actions>
          <v-btn variant="outlined" @click="addCart()"> 加入購物車 </v-btn>
        </v-card-actions> -->
        <!-- <v-card-actions>
          <v-select
            v-model="quantity"
            :items="quantityOptions"
            label="數量"
          ></v-select>
          <v-btn variant="outlined" @click="addCart()">加入購物車</v-btn>
        </v-card-actions> -->
      </v-card>
    </v-container>
  </div>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { useRouter } from "vue-router";
import { computed, defineComponent, reactive, ref } from "vue";
import ProductDataService from "../services/ProductDataService";
import { AddToCart } from "../models/user/product";
import Product from "../models/user/product";

export default defineComponent({
  name: "ManageProduct",
  setup() {
    const router = useRouter();
    const productList = reactive<Product[]>([]);

    // const currentProduct = {} as Product;
    // const quantity = ref(1);
    // const quantityOptions = [1, 2, 3, 4, 5];
    // const product_id = 1;

    // const currentProduct = reactive({
    //   quantity: 1,
    // } as AddToCart);

    return {
      router,
      productList,
      // quantity,
      // quantityOptions,
      // currentProduct,
      // product_id,
    };
  },
  methods: {

    // addCart() {
    //   const data: AddToCart = {
    //     product_id: this.currentProduct.product_id,
    //     market_id: this.currentProduct.market_id,
    //     user_id: this.currentProduct.user_id,
    //     quantity: this.currentProduct.quantity,
    //   };
    //   ProductDataService.ProductToCart(data)
    //     .then((response: any) => {
    //       console.log(response);
    //       this.router.push({ name: 'Cart' });
    //     })
    //     .catch((e: Error) => {
    //       console.log(e);
    //     });
    // },
  },
});
</script>

<style scoped>
.list-item-spacing {
  margin-bottom: 16px;
}
</style>
