<template>
  <v-container>
    <v-card elevation="2" tile max-width="500" class="ma-auto">
      <v-card-title>新增商品</v-card-title>
      <v-form class="ma-3">
        <v-text-field
          class="ma-3"
          v-model="state.product_name"
          label="商品名稱"
          :error-messages="v$.product_name.$errors.map((e: any) => e.$message)"
          @input="v$.product_name.$touch"
          @blur="v$.product_name.$touch"
        ></v-text-field>

        <v-select
          class="ma-3"
          v-model="state.category"
          :items="categoryList"
          label="種類"
        ></v-select>

        <v-text-field
          class="ma-3"
          v-model="state.brand"
          label="品牌"
          :error-messages="v$.brand.$errors.map((e: any) => e.$message)"
          @input="v$.brand.$touch"
          @blur="v$.brand.$touch"
        ></v-text-field>

        <v-text-field
          class="ma-3"
          v-model="state.price"
          label="價格"
          type="number"
          :error-messages="v$.price.$errors.map((e: any) => e.$message)"
          @input="v$.price.$touch"
          @blur="v$.price.$touch"
        ></v-text-field>

        <v-text-field
          class="ma-3"
          v-model="state.stock"
          label="庫存"
          type="number"
          :error-messages="v$.stock.$errors.map((e: any) => e.$message)"
          @input="v$.stock.$touch"
          @blur="v$.stock.$touch"
        ></v-text-field>
        <v-card-actions class="justify-end">
          <v-btn variant="tonal" color="blue-lighten-1" @click="saveProduct"
            >新增商品
          </v-btn>
          <v-btn variant="tonal" @click="back()">取消 </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required, minValue } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";
import { CreateProduct } from "../../../models/product/create-product";
import MarketDataService from "../../../services/MarketDataService";
import ProductDataService from "../../../services/ProductDataService";
import { PrdouctCategory } from "../../../models/product/product-category";

export default defineComponent({
  name: "create-product",
  setup() {
    const router = useRouter();

    const state = reactive({
      product_name: "",
      category: PrdouctCategory.居家生活,
      brand: "",
      price: 1,
      stock: 1,
      status: false,
      market_id: 0,
    });

    const rules = computed(() => {
      return {
        product_name: { required },
        category: { required },
        brand: { required },
        price: { required, minValue: minValue(0) },
        stock: { required, minValue: minValue(1) },
      };
    });

    const v$ = useValidate(rules, state);

    const categoryList = Object.values(PrdouctCategory);

    return { state, router, v$, categoryList };
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

    back() {
      this.router.push("/manage/product");
    },
  },
});
</script>
