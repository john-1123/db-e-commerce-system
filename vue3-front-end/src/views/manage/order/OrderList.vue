<template>
  <v-container>
    <v-card-title> [Management] Order List </v-card-title>
    <v-table>
      <thead>
        <tr>
          <th>OrderID</th>
          <th>State</th>
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
          <th>Detail</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orderList">
          <td>{{ order.order_id }}</td>
          <td>{{ order.state }}</td>
          <td>{{ order.items }}</td>
          <td>{{ order.cashs }}</td>
          <td>{{ order.quntities }}</td>
          <td>{{ order.cost }}</td>
          <td>
            <v-icon icon="fa:fas fa-edit" @click="detail(order)"></v-icon>
          </td>
          <td>
            <v-icon
              icon="fa:fas fa-trash"
              @click="deleteOrder(order.order_id)"
            ></v-icon>
          </td>
        </tr>
      </tbody>
    </v-table>
  </v-container>
  <v-container>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title> Order Details </v-card-title>
        <v-card-text>
          <v-card-item>
            Create Time: {{ selectedOrder.create_time }}
          </v-card-item>
          <v-card-item> Consignee: {{ selectedOrder.consignee }} </v-card-item>
          <v-card-item>
            Shipping Address: {{ selectedOrder.shipping_address }}
          </v-card-item>
          <v-card-item>
            Payment Method: {{ selectedOrder.payment_method }}
          </v-card-item>
          <v-card-item>
            Transport: {{ selectedOrder.mode_of_transport }}
          </v-card-item>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="close">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Order from "../../../models/order/order";
import MarketDataService from "../../../services/MarketDataService";
import OrderDataService from "../../../services/OrderDataService";

export default defineComponent({
  data() {
    return {
      orderList: [] as Order[],
      selectedOrder: {} as Order,
      dialog: false,
    };
  },

  mounted() {
    this.getOrders();
  },

  methods: {
    getOrders() {
      const userId = Number(sessionStorage.getItem("user"));
      if (userId) {
        MarketDataService.getMarketByUser(userId).then((response: any) => {
          const market_id = response.data.market_id;
          OrderDataService.getByMarket(market_id)
            .then((response: any) => {
              this.orderList = response.data;
            })
            .catch((e: Error) => {
              console.log(e);
            });
        });
      }
    },

    detail(order: Order) {
      console.log(order);
      this.selectedOrder = order;
      this.dialog = true;
    },

    close() {
      this.dialog = false;
    },

    deleteOrder(orderId: number) {
      OrderDataService.delete(orderId)
        .then((response: any) => {
          console.log(response.data);
          this.getOrders();
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },
  },
});
</script>
