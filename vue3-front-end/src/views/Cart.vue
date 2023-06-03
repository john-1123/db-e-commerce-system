<template>
  <v-container>
    <h1 class="text-center ma-3">Cart List</h1>
    <v-row class="mx-3 my-5" v-for="market in getGroupByMarket()">
      <v-col cols="12" class="d-flex">
        <h2>{{ getMarketName(market[0].market_id) }}</h2>
        <v-btn class="mx-5" color="orange-lighten-4">下訂單</v-btn>
      </v-col>
      <v-col>
        <v-table>
          <thead>
            <tr>
              <th>Product Name</th>
              <th>Category</th>
              <th>Brand</th>
              <th>Stock</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in getProductList(market[0].market_id)">
              <td>{{ item.product.product_name }}</td>
              <td>{{ item.product.category }}</td>
              <td>{{ item.product.brand }}</td>
              <td>{{ item.product.stock }}</td>
              <td>NTD$ {{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>{{ item.product.price * item.quantity }}</td>
              <td>
                <v-icon
                  icon="fa:fas fa-trash"
                  @click="
                    deleteItem(item.product.market_id, item.product.product_id)
                  "
                ></v-icon>
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
    </v-row>
  </v-container>
  <!-- <v-dialog v-model="BuyshowDialog" max-width="500">
      <v-card>
        <v-card-title>
          <span class='headline'>Order Details</span>
        </v-card-title>
        <v-card-text>
          <div v-for="(order, productID) in buyshoworder" :key="productID">
            <p>
              Product : {{ BuyshowDialog && order.product_name }}
              &nbsp;
              &nbsp;
              &nbsp;
              <p>Price: {{ BuyshowDialog && order.price }}
              Quantity:<input type="number" v-model="order.quantity" min="0"></p>
            </p>
            <br>
          </div>
          <v-text-field v-model="consignee" label="Consignee"></v-text-field>
          <br>
          <v-text-field v-model="shippingAddress" label="Shipping Address"></v-text-field>
          <br>
          <v-text-field v-model="mode_of_transport" label="Transport"></v-text-field>
          <br>
          <v-text-field v-model="payment" label="Payment method"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn color="tan" @click="submitOrder">
            Submit
          </v-btn>
          <v-btn color="tan" @click="closeBuy">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog> -->
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CartItem from "../models/cart/CartItem";
import Cart from "../models/cart/cart";
import CartDataService from "../services/CartDataService";
import MarketDataService from "../services/MarketDataService";
import ProductDataService from "../services/ProductDataService";

export default defineComponent({
  setup() {},

  data() {
    return {
      BuyshowDialog: false,
      buyshoworder: {},
      deletorder: {},
      consignee: "",
      shippingAddress: "",
      mode_of_transport: "",
      payment: "",

      cartList: [] as Cart[],
      marketMap: new Map<number, string>() as Map<number, string>,
      itemMap: new Map<number, CartItem[]>() as Map<number, CartItem[]>,
    };
  },

  methods: {
    getCart() {
      const userId = Number(sessionStorage.getItem("user"));
      if (userId) {
        CartDataService.getByUser(userId)
          .then((response: any) => {
            this.cartList = response.data;
            this.cartList.forEach((cart: Cart) => {
              if (!this.marketMap.has(cart.market_id)) {
                MarketDataService.get(cart.market_id)
                  .then((response: any) => {
                    this.marketMap.set(
                      cart.market_id,
                      response.data.market_name
                    );
                  })
                  .catch((e: Error) => {
                    console.log(e);
                  });
              }

              this.itemMap.set(cart.market_id, []);
              if (this.itemMap.has(cart.market_id)) {
                ProductDataService.get(cart.product_id)
                  .then((response: any) => {
                    this.itemMap.get(cart.market_id)?.push({
                      product: response.data,
                      quantity: cart.quntity,
                    });
                  })
                  .catch((e: Error) => {
                    console.log(e);
                  });
              }
            });
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    getGroupByMarket() {
      return this.groupBy(this.cartList, "market_id");
    },

    getProductList(marketId: number) {
      return this.itemMap.get(marketId);
    },

    getMarketName(marketId: number) {
      return this.marketMap.get(marketId);
    },

    groupBy(array: any, key: any) {
      // Return the end result
      return array.reduce((result: any, currentValue: any) => {
        // If an array already present for key, push it to the array. Else create an array and push the object
        (result[currentValue[key]] = result[currentValue[key]] || []).push(
          currentValue
        );
        // Return the current iteration `result` value, this will be taken as next iteration `result` value and accumulate
        return result;
      }, {}); // empty object is the initial value for result object
    },

    deleteItem(marketId: number, productId: number) {
      const userId = 1;
    },

    buy(marketId: number) {
      // this.buyshoworder = {};
      // for (const item of items) {
      //   const productID = item.product_id;
      //   if (!this.buyshoworder[productID]) {
      //     this.buyshoworder[productID] = {
      //       product_name: item.product_name,
      //       price: item.price,
      //       stock: item.stock,
      //       quantity: item.quantity,
      //     };
      //   }
      // }
      // console.log(this.buyshoworder);
      // this.BuyshowDialog = true;
    },

    // submitOrder() {
    //   if (!this.consignee || !this.shippingAddress || !this.mode_of_transport || !this.payment) {
    //     console.log("Requirement");
    //     return;
    //   }

    //   for(const [productID, order] of Object.entries(this.buyshoworder)){
    //     const quantity = parseInt(order.quantity);
    //     const stock = parseInt(order.stock);
    //     if (quantity > stock) {
    //       console.log("Do not buy more.");
    //       return;
    //     }
    //   }

    //   const orderData = {};
    //   for (const [productID, order] of Object.entries(this.buyshoworder)) {
    //     orderData[productID] = {
    //       product_id: order.product_id,
    //       price: order.price,
    //       quantity: order.quantity,
    //       stock: order.stock,
    //     }
    //   }

    //   orderData.consignee = this.consignee;
    //   orderData.shipping_address = this.shippingAddress;
    //   orderData.mode_of_transport = this.mode_of_transport;
    //   orderData.payment_method = this.payment;
    //   orderData.create_time = new Date().getTime();
    //   orderData.last_modified_time = new Date().getTime();

    //   this.placeOrder(orderData);
    //   this.BuyshowDialog = false;
    //   this.consignee = "";
    //   this.shippingddress = "";
    //   this.mode_of_transport = "";
    //   this.payment = ""
    // },

    // placeOrder(orderData) {
    //   axios
    //     .post("http://localhost:3000/detailorder", orderData)
    //     .then((res) => {
    //       console.log("Order placed successfully!");
    //     })
    //     .catch((error) => {
    //       console.log("Error placing the order. Please try again.");
    //     })
    // },

    // closeBuy() {
    //   this.buyshoworder = {};
    //   this.BuyshowDialog = false;
    //   this.consignee = "";
    //   (this.shippingAddress = ""),
    //     (this.mode_of_transport = ""),
    //     (this.payment = "");
    // },
  },

  mounted() {
    this.getCart();
  },
});
</script>
