<template>
  <div>
    <v-container>
      <v-row
        class="list px-3 mx-auto"
        style="height: 100px"
        justify="space-between"
      >
        <v-col cols="auto">
          <v-card-title class="mb-2">
            <p class="text-md-center">[Management] Product List</p>
          </v-card-title>
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="auto">
          <v-btn color="orange-lighten-4" class="ml-8" @click="CreateProduct">
            建立產品
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
  <!-- <v-text-field
          class="ma-3"
          v-model="productList[2].status"
          label="Product Name"
          :error-messages="v$.product_name.$errors.map((e: any) => e.$message)"
          @input="v$.product_name.$touch"
          @blur="v$.product_name.$touch"
    ></v-text-field> -->

  <v-table>
    <thead>
      <tr>
        <th class="text-left">Product Name</th>
        <th class="text-left">Category</th>
        <th class="text-left">Brand</th>
        <th class="text-left">Price</th>
        <th class="text-left">Stock</th>
        <th class="text-left">Status</th>
        <th class="text-left">Edit</th>
        <th class="text-left">Delete</th>
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
          <v-row justify="center">
            <v-icon
              @click="ChangeStatus(!product.status)"
              :icon="product.status ? 'fa:fas fa-lock-open' : 'fa:fas fa-lock'"
            ></v-icon>
          </v-row>
        </td>
        <td>
          <v-row>
            <v-btn color="blue-grey-lighten-2" @click="dialog = true">
              <v-icon icon="fa:fas fa-edit"></v-icon>
            </v-btn>
            <v-dialog v-model="dialog" persistent width="1024">
              <v-card>
                <v-card-title>
                  <span class="text-h5">Edit Product</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field
                          v-model="product.product_name"
                          label="Name*"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          v-model="product.category"
                          label="Category*"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          v-model="product.brand"
                          label="Brand*"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          v-model="product.price"
                          label="Price*"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          v-model="product.stock"
                          label="Stock*"
                          required
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="dialog = false"
                  >
                    Close
                  </v-btn>
                  <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="
                      UpdateProduct();
                      dialog = false;
                    "
                  >
                    Save
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
        </td>
        <td>
          <v-row>
            <v-icon icon="fa:fas fa-trash" @click="deleteProduct"></v-icon>
          </v-row>
        </td>
        <td></td>
      </tr>
    </tbody>
  </v-table>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { useRouter } from "vue-router";
import { computed, defineComponent, reactive } from "vue";
import ProductDataService from "../services/ProductDataService";
import Product from "../models/user/product";
import { UpdateProduct } from "../models/user/product";

export default defineComponent({
  name: "ManageProduct",
  setup() {
    const router = useRouter();
    const productList = reactive<Product[]>([]);
    // const product = {} as Product;

    const state = reactive({
      product_name: "",
      category: "",
      brand: "",
      price: 0,
      stock: 0,
    } as UpdateProduct);

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
    const product_id = 1;
    if (product_id) {
      ProductDataService.getAll().then((response: any) => {
        console.log(response);
        response.map((product: Product) => {
          productList.push(product);
        });

        // state.product_name = response["product_name"];
        // state.category = response["category"];
        // state.brand = response["brand"];
        // state.price = response["price"];
        // state.stock = response["stock"];
      });
    }

    return { router, product_id, state, v$, productList };
  },

  data() {
    return { dialog: false };
  },

  methods: {
    ChangeStatus(status: boolean) {
      //參數還需要加上id: number
      let data = {
        product_id: this.state.product_id,
        product_name: this.state.product_name,
        category: this.state.category,
        brand: this.state.brand,
        price: this.state.price,
        stock: this.state.stock,
        market_id: this.state.market_id,
        status: this.state.status,
      };

      ProductDataService.update(this.state.product_id, data)
        .then((response: any) => {
          this.state.status = status;
          console.log(response.data);
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },

    UpdateProduct() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const product: UpdateProduct = {
          product_id: this.state.product_id,
          product_name: this.state.product_name,
          category: this.state.category,
          brand: this.state.brand,
          price: this.state.price,
          stock: this.state.stock,
          market_id: this.state.market_id,
          status: this.state.status,
        };

        ProductDataService.update(this.product_id, product)
          .then((response: any) => {
            console.log(response);
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    CreateProduct() {
      this.router.push({ name: "CreateProduct" });
    },

    // getDisplayProduct(products: {
    //   id: any;
    //   product_name: string;
    //   category: string;
    //   price: number;
    //   stock: number;
    // }) {
    //   return {
    //     id: products.id,
    //     product_name:
    //       products.product_name.length > 30
    //         ? products.product_name.substr(0, 30) + "..."
    //         : products.product_name,
    //     category:
    //       products.category.length > 30
    //         ? products.category.substr(0, 30) + "..."
    //         : products.category,
    //     price: products.price,
    //     stock: products.stock,
    //   };
    // },
    // retrieveProductList() {
    //     ProductDataService.getAll()
    //       .then((response) => {
    //     this.products = response.data.map(this.getDisplayProduct);
    //     console.log(response.data);
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // },

    deleteProduct() {},
    // deleteProduct() {
    //     ProductDataService.delete(this.product.product_id)
    //     .then((response) => {
    //       console.log(response.data);
    //       this.router.push({name: 'product'})
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // },
  },
});
</script>

<style>
.list {
  max-width: 750px;
}
</style>
