<template>
  <v-container>
    <h1 class="text-center ma-3">Cart List</h1>
    <v-row class="mx-3 my-5" v-for="market in getGroupByMarket()">
      <v-col cols="12" class="d-flex">
        <h2>{{ getMarketName(market[0].market_id) }}</h2>
        <v-btn
          class="mx-5"
          color="orange-lighten-4"
          @click="buyOrder(market[0].market_id)"
          >下訂單</v-btn
        >
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
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
      <v-card-title>Order Details</v-card-title>
      <v-card-text>
        <v-card-item v-for="item in orderItemList">
          {{ itemLine(item) }}
        </v-card-item>

        <v-text-field
          class="my-3"
          v-model="state.consignee"
          label="Consignee"
          :error-messages="v$.consignee.$errors.map((e: any) => e.$message)"
          @input="v$.consignee.$touch"
          @blur="v$.consignee.$touch"
        ></v-text-field>

        <v-text-field
          class="my-3"
          v-model="state.shippingAddress"
          label="Shipping Address"
          :error-messages="v$.shippingAddress.$errors.map((e: any) => e.$message)"
          @input="v$.shippingAddress.$touch"
          @blur="v$.shippingAddress.$touch"
        ></v-text-field>

        <v-select
          class="my-3"
          v-model="state.modeOfTransport"
          :items="transportList"
          label="Mode of Transport"
        ></v-select>

        <v-select
          class="my-3"
          v-model="state.paymentMethod"
          :items="paymentList"
          label="Payment method"
        ></v-select>

        <v-card-actions class="justify-space-between">
          <v-btn color="blue-lighten-1" @click="onSubmit">Submit</v-btn>
          <v-btn @click="close">Close</v-btn>
        </v-card-actions>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import CartItem from "../models/cart/CartItem";
import Cart from "../models/cart/cart";
import { TransportMode } from "../models/cart/transport-mode";
import CartDataService from "../services/CartDataService";
import MarketDataService from "../services/MarketDataService";
import ProductDataService from "../services/ProductDataService";
import { PaymentMode } from "../models/cart/payment-mode";
import CreateOrder from "../models/order/create-order";
import OrderDataService from "../services/OrderDataService";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const router = useRouter();

    const state = reactive({
      consignee: "",
      shippingAddress: "",
      modeOfTransport: TransportMode.SevenEleven,
      paymentMethod: PaymentMode.Visa,
    });

    const rules = computed(() => {
      return {
        consignee: { required },
        shippingAddress: { required },
        modeOfTransport: { required },
        paymentMethod: { required },
      };
    });

    const transportList = Object.values(TransportMode);
    const paymentList = Object.values(PaymentMode);

    const v$ = useValidate(rules, state);

    return { router, transportList, paymentList, state, v$ };
  },

  data() {
    return {
      cartList: [] as Cart[],
      marketMap: new Map<number, string>() as Map<number, string>,
      itemMap: new Map<number, CartItem[]>() as Map<number, CartItem[]>,
      orderItemList: [] as CartItem[],
      dialog: false,
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
      const userId = Number(sessionStorage.getItem("user"));
      if (userId) {
        CartDataService.delete(userId, marketId, productId)
          .then((response: any) => {
            console.log(response.data);
            this.getCart();
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    buyOrder(marketId: number) {
      this.orderItemList = this.itemMap.get(marketId)!;
      this.dialog = true;
    },

    itemLine(item: CartItem) {
      return `產品: ${item.product.product_name} / 價錢: ${item.product.price} / 數量: ${item.quantity}`;
    },

    onSubmit() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const userId = Number(sessionStorage.getItem("user"));
        if (userId) {
          const order: CreateOrder = {
            member_id: userId,
            market_id: this.orderItemList[0].product.market_id,
            state: "待確認",
            shipping_address: this.state.shippingAddress,
            consignee: this.state.consignee,
            payment_method: this.state.paymentMethod,
            mode_of_transport: this.state.modeOfTransport,
          };
          OrderDataService.create(order)
            .then((response: any) => {
              console.log(response.data);
              this.router.push("/orders");
            })
            .catch((e: Error) => {
              console.log(e);
            });
        }
      }
    },

    close() {
      this.dialog = false;
      this.state.consignee = "";
      this.state.shippingAddress = "";
      this.state.modeOfTransport = TransportMode.SevenEleven;
      this.state.paymentMethod = PaymentMode.Visa;
      this.v$.$reset();
    },
  },

  mounted() {
    this.getCart();
  },
});
</script>
