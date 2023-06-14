<template>
  <v-container>
    <h1 class="text-center ma-3">我的訂單</h1>
    <v-table>
      <thead>
        <tr>
          <th>訂單編號</th>
          <th>狀態</th>
          <th>建立時間</th>
          <th>小計</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orderList">
          <td>{{ order.order_id }}</td>
          <td>{{ order.state }}</td>
          <td>{{ order.create_time }}</td>
          <td>{{ order.cost }}</td>
          <td>
            <v-icon icon="fa:fas fa-edit" @click="detail(order)"></v-icon>
          </td>
          <td>
            <v-icon icon="fa:fas fa-trash" @click="deleteOrder(order)"></v-icon>
          </td>
        </tr>
      </tbody>
    </v-table>
  </v-container>
  <v-container>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title>訂單編號 : {{ selectedOrder.order_id }}</v-card-title>
        <v-card-text>
          <v-card-item>
            建立時間 : {{ selectedOrder.create_time }}
          </v-card-item>
          <v-card-item> 收貨人 : {{ selectedOrder.consignee }} </v-card-item>
          <v-card-item>
            付款方式 : {{ selectedOrder.payment_method }}
          </v-card-item>
          <v-card-item>
            運送方式 : {{ selectedOrder.mode_of_transport }}
          </v-card-item>
          <v-card-item>
            運送地址 : {{ selectedOrder.shipping_address }}
          </v-card-item>
          <v-card-item>
            購買細項 :
            <v-list :items="getItemList()"></v-list>
          </v-card-item>
          <v-card-item> 小計 : {{ selectedOrder.cost }} 元 </v-card-item>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn variant="tonal" color="blue" @click="checkOrder"
            >訂單已完成
          </v-btn>
          <v-btn variant="tonal" @click="dialog = false">關閉</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import OrderDataService from "../services/OrderDataService";
import Order from "../models/order/order";
import { OrderState } from "../models/order/order-state";
import { UpdateOrderState } from "../models/order/update-order-state";

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
        OrderDataService.getByUser(userId)
          .then((response: any) => {
            console.log(response.data);
            this.orderList = response.data;
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    detail(order: Order) {
      console.log(order);
      this.selectedOrder = order;
      this.dialog = true;
    },

    deleteOrder(order: Order) {
      if (order.state == OrderState.待確認) {
        OrderDataService.delete(order.order_id)
          .then((response: any) => {
            console.log(response.data);
            this.getOrders();
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    getItemList() {
      const itemList = [];
      const productList = this.selectedOrder.items.split(",");
      const quantityList = this.selectedOrder.quantities.split(",");
      const cashList = this.selectedOrder.cashs.split(",");
      for (let i = 0; i < productList.length; i++) {
        itemList.push(
          `${productList[i]}, ${quantityList[i]}個, ${cashList[i]}元`
        );
      }
      return itemList;
    },

    checkOrder() {
      if (this.selectedOrder.state == OrderState.配送中) {
        const state = {
          state: OrderState.已完成,
        } as UpdateOrderState;
        OrderDataService.update(this.selectedOrder.order_id, state)
          .then((response: any) => {
            this.dialog = false;
            this.getOrders();
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },
  },
});
</script>
