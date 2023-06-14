<template>
  <v-container v-if="marketId">
    <v-card-title> [Management] 賣家管理訂單 </v-card-title>
    <v-card-subtitle>Market Name : {{ marketName }}</v-card-subtitle>
    <v-table>
      <thead>
        <tr>
          <th>訂單編號</th>
          <th>狀態</th>
          <th>建立時間</th>
          <th>收貨人</th>
          <th>小計</th>
          <th></th>
          <!-- <th></th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orderList">
          <td>{{ order.order_id }}</td>
          <td>{{ order.state }}</td>
          <td>{{ order.create_time }}</td>
          <td>{{ order.consignee }}</td>
          <td>{{ order.cost }}</td>
          <td>
            <v-icon icon="fa:fas fa-edit" @click="detail(order)"></v-icon>
          </td>
          <!-- <td>
            <v-icon icon="fa:fas fa-trash" @click="deleteOrder(order)"></v-icon>
          </td> -->
        </tr>
      </tbody>
    </v-table>
  </v-container>
  <v-container v-if="!marketId">
    <CreateMarket></CreateMarket>
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
          <v-card-item> 訂單狀態 : {{ selectedOrder.state }} </v-card-item>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn variant="tonal" color="blue" @click="checkOrder"
            >確認訂單
          </v-btn>
          <v-btn variant="tonal" @click="dialog = false">關閉</v-btn>
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
import CreateMarket from "../product/CreateMarket.vue";
import { OrderState } from "../../../models/order/order-state";
import { UpdateOrderState } from "../../../models/order/update-order-state";

export default defineComponent({
  name: "ManageOrder",
  components: {
    CreateMarket,
  },
  data() {
    return {
      orderList: [] as Order[],
      selectedOrder: {} as Order,
      dialog: false,
      marketId: null,
      marketName: "",
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
          const marketId = response.data.market_id;
          this.marketName = response.data.market_name;
          if (marketId) {
            this.marketId = marketId;
            OrderDataService.getByMarket(marketId)
              .then((response: any) => {
                this.orderList = response.data;
              })
              .catch((e: Error) => {
                console.log(e);
              });
          }
        });
      }
    },

    detail(order: Order) {
      this.selectedOrder = order;
      this.dialog = true;
    },

    deleteOrder(order: Order) {
      OrderDataService.delete(order.order_id)
        .then((response: any) => {
          this.getOrders();
        })
        .catch((e: Error) => {
          console.log(e);
        });
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
      if (this.selectedOrder.state == OrderState.待確認) {
        const state = {
          state: OrderState.配送中,
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
