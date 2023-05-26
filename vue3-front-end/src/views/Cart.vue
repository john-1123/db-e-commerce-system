<template>
  <div class="cart-container">
    <h2>Cart List</h2>
    <div v-for="(items, marketId) in cartItemsByMarket" :key="marketId" class="market-container">
      <div class="market-header">
        <h2>{{ marketId }}</h2>
        <div class="action-buttons">
          <p>
            <button @click="buy(items)" color="tan" class='button'>
              GO! BUY!
            </button>
          </p>
          <p>
            <button @click="delet(marketId)" color="tan" class='button'>
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
                Product: {{ item.product_id }}
                &nbsp;
                &nbsp;
                &nbsp;
                Price: {{ item.price }}
                Quantity: {{ item.quantity }}
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
              Product ID: {{ BuyshowDialog && order.product_id }}
              &nbsp;
              &nbsp;
              &nbsp;
              Price: {{ BuyshowDialog && order.price }}
              Quantity: {{ BuyshowDialog && order.quantity }}
            </p>
            <br>
          </div>
          <v-text-field v-model="consignee" label="Consignee"></v-text-field>
          <br>
          <v-text-field v-model="shippingAddress" label="Shipping Address"></v-text-field>
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
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return { 
      cartItems: [],
      BuyshowDialog: false,
      buyshoworder: {},
      consignee: "",
      shippingAddress: ""
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
            product_id: item.product_id,
            price: item.price,
            quantity: item.quantity
          };
        }
      }
      //console.log(this.buyshoworder);
      this.BuyshowDialog = true;
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
      this.shippingAddress = ""
    },

    submitOrder() {
      if (!this.consignee || !this.shippingAddress) {
        console.log("Requirement");
        return;
      }
      const orderData = {};
      for (const [productID, order] of Object.entries(this.buyshoworder)) {
        orderData[productID] = {
          product_id: order.product_id,
          price: order.price,
          quantity: order.quantity,
        };
      }
      orderData.consignee = this.consignee;
      orderData.shipping_address = this.shippingAddress;
      orderData.timestamp = new Date().getTime();
      
      this.placeOrder(orderData);
      this.BuyshowDialog = false;
      this.consignee = ""; 
      this.shippingAddress = "";
    },

    delet(marketId) {
      axios.post('http://localhost:3000/consignee', { market_id: marketId })
      .then((res) => {
        console.log('Successful delete data.');
      })
      .catch((error) => {
        console.log('Error delete data.');
      });
      pass
    },
  },
 
  computed: {
    cartItemsByMarket() {
      const itemsByMarket = {};
      for (const item of this.cartItems) {
        const marketId = item.market_id;
        if (!itemsByMarket[marketId]) {
          itemsByMarket[marketId] = [];
          itemsByMarket[marketId].push(item);
        }else{
          itemsByMarket[marketId].push(item);
        }
      }
      return itemsByMarket;
    },
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

