<template>
  <div class="cart-container">
    <h2>Cart List</h2>
    <div v-for="(items, marketName) in cartItemsByMarket" :key="marketName" class="market-container">
      <div class="market-header">
        <h2>{{ marketName }}</h2>
        <div class="action-buttons">
          <p>
            <button @click="buy(items)" color="tan" class='button'>
              GO! BUY!
            </button>
          </p>
          <p>
            <button @click="delet(items)" color="tan" class='button'>
            Delete
            </button>
          </p>
        </div>
      </div>
      <div class="market-content">
        <div v-for="item in items" :key="item.product_id" class="product-item">
          <div class="product-info">
            <div class="center-section">
              <p>
                Product: {{ item.product_name }}
                &nbsp;
                &nbsp;
                &nbsp;
                Price: {{ item.price }}
                Stock: {{ item.stock }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <v-dialog v-model="BuyshowDialog" max-width="500">
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
    </v-dialog>
    <!-- 根据用户角色显示订单列表 
      <v-pagination v-model="currentPage" :total-visible="itemsPerPage" :length="totalPages">
      </v-pagination>
    -->
  </div>
</template>


<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  data() {
    return { 
      cartItems: [],
      BuyshowDialog: false,
      buyshoworder: {},
      deletorder : {},
      consignee: "",
      shippingAddress: "",
      mode_of_transport:"",
      payment:"",
      //currentPage: 1,
      //itemsPerPage: 5, 
    };
  },

  mounted() {
    this.getCart();
  },

  methods: { 
    getCart() {
      axios.get('http://localhost:3000/carts')
        .then((res) => {
          this.cartItems = res.data;
          //console.log(cartItems);
        })
        .catch((error) => {
          console.log("No catch data.");
        });
    },

    buy(items) {
      this.buyshoworder = {};
      for (const item of items) {
        const productID = item.product_id;
        if (!this.buyshoworder[productID]) {
          this.buyshoworder[productID] = {
            product_name: item.product_name,
            price: item.price,
            stock: item.stock,
            quantity: item.quantity
          };
        }
      }
      console.log(this.buyshoworder);
      this.BuyshowDialog = true;
    },

    submitOrder() {
      if (!this.consignee || !this.shippingAddress || !this.mode_of_transport || !this.payment) {
        console.log("Requirement");
        return;
      }

      for(const [productID, order] of Object.entries(this.buyshoworder)){
        const quantity = parseInt(order.quantity);
        const stock = parseInt(order.stock);
        if (quantity > stock) {
          console.log("Do not buy more.");
          return;
        }
      }
      
      const orderData = {};
      for (const [productID, order] of Object.entries(this.buyshoworder)) {
        orderData[productID] = {
          product_id: order.product_id,
          price: order.price,
          quantity: order.quantity,
          stock: order.stock,
        }
      }

      orderData.consignee = this.consignee;
      orderData.shipping_address = this.shippingAddress;
      orderData.mode_of_transport = this.mode_of_transport;
      orderData.payment_method = this.payment;
      orderData.create_time = new Date().getTime();
      orderData.last_modified_time = new Date().getTime();
      
      this.placeOrder(orderData);
      this.BuyshowDialog = false;
      this.consignee = ""; 
      this.shippingddress = "";
      this.mode_of_transport = "";
      this.payment = ""
    },

    placeOrder(orderData) {
      axios
        .post("http://localhost:3000/detailorder", orderData)
        .then((res) => {
          console.log("Order placed successfully!");
        })
        .catch((error) => {
          console.log("Error placing the order. Please try again.");
        })
    },

    closeBuy() {
      this.buyshoworder = {};
      this.BuyshowDialog = false;
      this.consignee = ""; 
      this.shippingAddress = "",
      this.mode_of_transport = "",
      this.payment = ""
    },

    delet(items) {
      const deletorder = {};
      for (const item of items){
        const deletmarketID = item.market_id;
        const deletproductID = item.product_id;
        deletorder.market_id = this.deletmarketID;
        deletorder.product_id = this.deletproductID;
      }
      axios.post('http://localhost:3000/consignee', deletorder)
      .then((res) => {
        console.log('Successful delete data.');
      })
      .catch((error) => {
        console.log('Error delete data.');
      });
    },
  },
 
  computed: {
    cartItemsByMarket() {
      const itemsByMarket = {};
      for (const item of this.cartItems) {
        const marketName = item.market_name;
        if (!itemsByMarket[marketName]) {
          itemsByMarket[marketName] = [];
          itemsByMarket[marketName].push(item);
        }else{
          itemsByMarket[marketName].push(item);
        }
      }
      return itemsByMarket;
    },

    /*totalItems() {
      let totalCount = 0;
      for (const marketName in this.cartItemsByMarket) {
        totalCount += this.cartItemsByMarket[marketName].length;
      }
      return totalCount;
    },

    totalPages() {
      return Math.ceil(this.totalItems / this.itemsPerPage); 
    },

    displayedCartItems() {
      const start = (this.currentPage - 1) * this.itemsPerPage; 
      const end = start + this.itemsPerPage; 
      const displayedItems = [];
      for (const marketName in this.cartItemsByMarket) {
        const items = this.cartItemsByMarket[marketName].slice(start, end);
        displayedItems.push(...items);
      }
      return displayedItems; 
    },*/
  },
};
</script>

<style>
.cart-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.market-container {
  width: 50%;
  margin: 10px;
  border: 1px solid rgba(0, 0, 0, 0.2); 
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.market-header {
  flex: 1;
}

.market-content {
  flex: 2;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
}

.product-item {
  display: flex;
  margin-bottom: 10px;
}

.product-info {
  text-align: center;
  flex: 2;
  display: flex;
  justify-content: center;
}

.center-section {
    flex: 1;
    align-items: center;
}

.button {
  background-color: transparent;
  padding: 0;
  font-size: 20px;
  text-decoration: underline;
  color: black;
  cursor: pointer;
}

.button:hover {
  text-decoration: none;
  color: #555;
}
</style>

