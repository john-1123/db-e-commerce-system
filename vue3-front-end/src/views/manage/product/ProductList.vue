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
          <th>Product Name</th>
          <th>Category</th>
          <th>Brand</th>
          <th>Price</th>
          <th>Stock</th>
          <th>Status</th>
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
              color="deep-orange-lighten-3"
              @click="openDialog(product), (dialog = true)"
            >
              <v-icon icon="fa:fas fa-edit"></v-icon>
            </v-btn>
            <v-dialog v-model="dialog" persistent width="1024">
              <v-card>
                <v-card-title class="text-h5"> Edit Product </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field
                          v-model="state.product_name"
                          label="Name"
                          :error-messages="v$.product_name.$errors.map((e: any) => e.$message)"
                          @input="v$.product_name.$touch"
                          @blur="v$.product_name.$touch"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          v-model="state.category"
                          label="Category*"
                          :error-messages="v$.category.$errors.map((e: any) => e.$message)"
                          @input="v$.category.$touch"
                          @blur="v$.category.$touch"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          v-model="state.brand"
                          label="Brand*"
                          :error-messages="v$.brand.$errors.map((e: any) => e.$message)"
                          @input="v$.brand.$touch"
                          @blur="v$.brand.$touch"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          v-model="state.price"
                          label="Price*"
                          :error-messages="v$.price.$errors.map((e: any) => e.$message)"
                          @input="v$.price.$touch"
                          @blur="v$.price.$touch"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          v-model="state.stock"
                          label="Stock*"
                          :error-messages="v$.stock.$errors.map((e: any) => e.$message)"
                          @input="v$.stock.$touch"
                          @blur="v$.stock.$touch"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-row class="justify-end mx-3">
                    <v-btn
                      color="blue-darken-1"
                      variant="tonal"
                      @click="updateProduct()"
                    >
                      Save
                    </v-btn>
                    <v-btn
                      color="blue-darken"
                      variant="tonal"
                      @click="dialog = false"
                    >
                      Close
                    </v-btn>
                  </v-row>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </td>
          <td>
            <v-icon
              icon="fa:fas fa-trash"
              @click="deleteProduct(product.product_id)"
            ></v-icon>
          </td>
        </tr>
      </tbody>
    </v-table>
  </v-container>
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

export default defineComponent({
  name: "ManageProduct",
  components: {
    CreateMarket,
  },
  setup() {
    const router = useRouter();

    const state = reactive({
      product_name: "",
      category: "",
      brand: "",
      price: 0,
      stock: 0,
      status: false,
    } as UpdateProduct);

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

    return { router, state, v$ };
  },

  data() {
    return {
      dialog: false,
      productList: [] as Product[],
      selectedProductId: 0,
      marketId: null,
      marketName: "",
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
      this.state.category = product.category;
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

    deleteProduct(productId: number) {
      ProductDataService.delete(productId)
        .then((response: any) => {
          console.log(response);
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
