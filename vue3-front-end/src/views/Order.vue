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
          <td>NTD$ {{ order.cost.toLocaleString("zh-TW") }}</td>
          <td>
            <v-icon icon="fa:fas fa-edit" @click="detail(order)"></v-icon>
          </td>
          <td>
            <v-icon icon="fa:fas fa-trash" @click="openAlert(order)"></v-icon>
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
          <v-card-item>
            小計 : {{ selectedOrder.cost.toLocaleString("zh-TW") }} 元
          </v-card-item>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn
            variant="tonal"
            color="blue"
            :disabled="isDisabled"
            @click="checkOrder"
            >訂單已完成
          </v-btn>
          <v-btn variant="tonal" @click="dialog = false">關閉</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>

  <v-dialog v-model="alertDialog" max-width="500">
    <v-card>
      <v-card-title> 提示訊息 </v-card-title>
      <v-card-text>
        {{ message }}
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn
          color="blue"
          variant="tonal"
          :disabled="!canDeleted"
          @click="deleteOrder()"
          >確定</v-btn
        >
        <v-btn class="mx-3" variant="tonal" @click="alertDialog = false"
          >關閉</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
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
      alertDialog: false,
      message: "",
      isDisabled: false,
      canDeleted: true,
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
            this.orderList = response.data;
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    detail(order: Order) {
      this.selectedOrder = order;
      this.isDisabled = this.selectedOrder.state != OrderState.配送中;
      this.dialog = true;
    },

    openAlert(order: Order) {
      this.selectedOrder = order;
      this.canDeleted = this.selectedOrder.state != OrderState.配送中;
      this.message = `確定要刪除"訂單編號 : ${this.selectedOrder.order_id}"嗎 ?`;
      this.alertDialog = true;
    },

    deleteOrder() {
      if (this.selectedOrder.state != OrderState.配送中) {
        OrderDataService.delete(this.selectedOrder.order_id)
          .then((response: any) => {
            this.alertDialog = false;
            this.message = "";
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
