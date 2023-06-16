<template>
  <v-container v-if="marketId">
    <v-row justify="space-between">
      <v-col cols="auto">
        <v-card-title> [Management] 賣家管理商品 </v-card-title>
        <v-card-subtitle>Market Name : {{ marketName }}</v-card-subtitle>
      </v-col>
      <v-col cols="auto">
        <v-btn color="orange-lighten-4" @click="createProduct">
          建立產品
        </v-btn>
      </v-col>
    </v-row>
    <v-table>
      <thead>
        <tr>
          <th>產品名稱</th>
          <th>種類</th>
          <th>品牌</th>
          <th>價格</th>
          <th>庫存</th>
          <th>狀態</th>
          <th>Edit</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(product, index) in productList" :key="index">
          <td>{{ product.product_name }}</td>
          <td>{{ product.category }}</td>
          <td>{{ product.brand }}</td>
          <td>NTD$ {{ product.price.toLocaleString("zh-TW") }}</td>
          <td>{{ product.stock }}</td>
          <td>
            <v-icon
              @click="changeStatus(product)"
              :icon="product.status ? 'fa:fas fa-lock' : 'fa:fas fa-lock-open'"
            ></v-icon>
          </td>
          <td>
            <v-btn
              color="orange-lighten-1"
              @click="openDialog(product), (dialog = true)"
            >
              <v-icon icon="fa:fas fa-edit"></v-icon>
            </v-btn>
          </td>
          <td>
            <v-icon icon="fa:fas fa-trash" @click="openAlert(product)"></v-icon>
          </td>
        </tr>
      </tbody>
    </v-table>
  </v-container>

  <v-dialog v-model="dialog" persistent width="1024">
    <v-card>
      <v-card-title class="mx-3 mt-3 text-h5">編輯商品</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="state.product_name"
              label="商品名稱"
              :error-messages="v$.product_name.$errors.map((e: any) => e.$message)"
              @input="v$.product_name.$touch"
              @blur="v$.product_name.$touch"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="6">
            <v-select
              v-model="state.category"
              :items="categoryList"
              label="種類"
            ></v-select>
          </v-col>
          <v-col cols="12" sm="6" md="6">
            <v-text-field
              v-model="state.brand"
              label="品牌"
              :error-messages="v$.brand.$errors.map((e: any) => e.$message)"
              @input="v$.brand.$touch"
              @blur="v$.brand.$touch"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              v-model="state.price"
              label="價格"
              :error-messages="v$.price.$errors.map((e: any) => e.$message)"
              @input="v$.price.$touch"
              @blur="v$.price.$touch"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              v-model="state.stock"
              label="庫存"
              :error-messages="v$.stock.$errors.map((e: any) => e.$message)"
              @input="v$.stock.$touch"
              @blur="v$.stock.$touch"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions class="justify-end ma-3">
        <v-btn color="blue-darken-1" variant="tonal" @click="updateProduct()">
          儲存
        </v-btn>
        <v-btn color="blue-darken" variant="tonal" @click="dialog = false">
          關閉
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="alertDialog" max-width="500">
    <v-card>
      <v-card-title> 提示訊息 </v-card-title>
      <v-card-text>
        {{ message }}
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn color="blue" variant="tonal" @click="deleteProduct()"
          >確定</v-btn
        >
        <v-btn class="mx-3" variant="tonal" @click="alertDialog = false"
          >關閉</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-container v-if="!marketId">
    <CreateMarket></CreateMarket>
  </v-container>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";
import Product from "../../../models/product/product";
import { UpdateProduct } from "../../../models/product/update-prodcut";
import MarketDataService from "../../../services/MarketDataService";
import ProductDataService from "../../../services/ProductDataService";
import CreateMarket from "./CreateMarket.vue";
import { PrdouctCategory } from "../../../models/product/product-category";

export default defineComponent({
  name: "ManageProduct",
  components: {
    CreateMarket,
  },
  setup() {
    const router = useRouter();

    const state = reactive({
      product_name: "",
      category: PrdouctCategory.運動健身,
      brand: "",
      price: 0,
      stock: 0,
      status: false,
    });

    const rules = computed(() => {
      return {
        product_name: { required },
        category: { required },
        brand: { required },
        price: { required },
        stock: { required },
        status: { required },
      };
    });

    const v$ = useValidate(rules, state);

    const categoryList = Object.values(PrdouctCategory);

    return { router, state, v$, categoryList };
  },

  data() {
    return {
      dialog: false,
      productList: [] as Product[],
      selectedProductId: 0,
      marketId: null,
      marketName: "",
      alertDialog: false,
      message: "",
    };
  },

  methods: {
    getProducts() {
      const userId = Number(sessionStorage.getItem("user"));
      if (userId) {
        MarketDataService.getMarketByUser(userId)
          .then((response: any) => {
            const marketId = response.data.market_id;
            this.marketName = response.data.market_name;
            if (marketId) {
              this.marketId = marketId;
              ProductDataService.getProductByMarket(marketId)
                .then((response: any) => {
                  this.productList = response.data;
                })
                .catch((e: Error) => {
                  console.log(e);
                });
            }
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    changeStatus(product: Product) {
      product.status = !product.status;
      ProductDataService.update(product.product_id, product)
        .then((response: any) => {
          console.log(response);
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    openDialog(product: Product) {
      this.selectedProductId = product.product_id;
      this.state.product_name = product.product_name;
      this.state.category = Object.values(PrdouctCategory).find(
        (val: string) => val == product.category
      )!;
      this.state.brand = product.brand;
      this.state.price = product.price;
      this.state.stock = product.stock;
    },

    updateProduct() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const product: UpdateProduct = {
          product_name: this.state.product_name,
          category: this.state.category,
          brand: this.state.brand,
          price: this.state.price,
          stock: this.state.stock,
          status: this.state.status,
        };

        ProductDataService.update(this.selectedProductId, product)
          .then((response: any) => {
            console.log(response);
            this.dialog = false;
            this.getProducts();
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    createProduct() {
      this.router.push({ name: "CreateProduct" });
    },

    openAlert(product: Product) {
      this.selectedProductId = product.product_id;
      this.message = `確定要刪除"${product.product_name}"嗎?`;
      this.alertDialog = true;
    },

    deleteProduct() {
      ProductDataService.delete(this.selectedProductId)
        .then((response: any) => {
          this.message = "";
          this.alertDialog = false;
          this.getProducts();
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },

  mounted() {
    this.getProducts();
  },
});
</script>
