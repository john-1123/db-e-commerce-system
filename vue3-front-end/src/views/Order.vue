<template>
    <v-container>
        <div class="header"> 
            <h1>Order List</h1>
            <v-btn @click="toggleRole" color="tan">{{ role }}</v-btn>
        </div>
        <div v-if="role === 'Buyer'">
            <div v-for="order in displayedOrders" :key="order.order_id" >
                <div class="order-box">
                    <div class="order-details">
                        <div class="left-section">
                            <p>OrderID: &nbsp; &nbsp;  {{ order.order_id }}</p>
                            <p>State: &nbsp; {{ order.state }}</p> 
                        </div>
                        <div class="center-section">
                            <p>Market: {{ order.market_name }} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Product: {{ order.product_name }}</p>              
                            <p>Price: {{ order.price }} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; Quantity: {{ order.quantity }} </p>
                            <p>Total: {{ (parseFloat(order.price)) * parseFloat((order.quantity)) }} </p>
                        </div>
                        <div class="right-section">
                            <p>
                                <v-btn @click="showBuyerDetails(order)" color="tan">
                                    details
                                </v-btn>
                            </P>
                            <br>
                            <p>
                                <v-btn @click='deletBuyer(order)' color="tan">
                                    Delete
                                </v-btn>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <v-dialog v-model="BuyershowDialog" max-width="500">
                <v-card>
                    <v-card-title>
                        <span class="headline">Order Details</span>
                    </v-card-title>
                    <v-card-text>
                        <p>Payment Method: {{ BuyerselectedOrder && BuyerselectedOrder.payment_method }}</p>
                        <p>Shipping Address: {{ BuyerselectedOrder && BuyerselectedOrder.shipping_address }}</p>
                        <p>Transport: {{ BuyerselectedOrder && BuyerselectedOrder.mode_of_transport }}</p>
                        <p>Create Time: {{ BuyerselectedOrder && BuyerselectedOrder.create_time }}</p>
                        <p>Last Modified Time: {{ BuyerselectedOrder && BuyerselectedOrder.last_modified_time }}</p>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="tan" text @click="closeBuyerDetails">Close</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
        <div v-else>
            <div v-for="order in displayedOrders" :key="order.order_id">
                <div class="order-box">
                    <div class="order-sellerdetails">
                        <div class="left-sellersection">
                            <p>Consignee Information</p>
                            <p>Consignee: {{ order.consignee }}</p>
                            <p>Shipping Address: {{ order.shipping_address }}</p>
                            <p>Phone: {{ order.phone }}</p>
                        </div>
                        <div class="center-sellersection">
                            <p>Product Information</p>
                            <p>Product: {{ order.product_name }}</p>
                            <p>Price: {{ order.price }}</p>
                            <p>State: {{ order.state }}</p>
                        </div>
                        <div class="right-sellersection">
                            <v-btn @click="showSellerDetails(order)" color="tan" small>
                                DetailS
                            </v-btn>
                            &nbsp;
                            <v-btn @click='deletSeller(order)' color="tan">
                                Delete
                            </v-btn>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <v-dialog v-model="SellershowDialog" max-width="500">
            <v-card>
                <v-card-title>
                    <span class="headline">Order Details</span>
                </v-card-title>
                <v-card-text>
                    <p>Create Time: {{ SellerselectedOrder && SellerselectedOrder.create_time }}</p>
                    <p>Last Modified Time: {{ SellerselectedOrder && SellerselectedOrder.last_modified_time }}</p>
                    <p>Shipping Address: {{ SellerselectedOrder &&  SellerselectedOrder.shipping_address }}</p>
                    <p>Payment Method: {{ SellerselectedOrder && SellerselectedOrder.payment_method }}</p>
                    <p>Transport: {{ SellerselectedOrder && SellerselectedOrder.mode_of_transport }}</p>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="tan" text @click="closeSellerDetails">
                        Close
                    </v-btn>
                    <div v-if="SellershowDialog"></div>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-pagination v-model="currentPage" :total-visible="itemsPerPage" :length="totalPages" class="fixed-pagination">
        </v-pagination>
    </v-container>
</template>
  
<script lang="ts">
import axios from 'axios';
  
export default {
    data() {
        return {
            role: 'Buyer',
            orderInformation: [],
            SellershowDialog: false,
            BuyershowDialog: false,
            SellerselectedOrder: null,
            BuyerselectedOrder: null,
            currentPage: 1, 
            itemsPerPage: 3,
        };
    },
  
    mounted() {
        this.getOrders();
    },

    computed: {
    totalItems() {
      return this.orderInformation.length;
    },
    totalPages() {
      return Math.ceil(this.totalItems / this.itemsPerPage); 
    },
    displayedOrders() {
      const start = (this.currentPage - 1) * this.itemsPerPage; 
      const end = start + this.itemsPerPage; 
      return this.orderInformation.slice(start, end); 
    },
  },
  
    methods: {
        getOrders() {
            const apiUrl = this.role === 'Buyer' ? 'http://localhost:3000/order_buyer' : 'http://localhost:3000/order_seller';
            axios
            .get(apiUrl)
            .then((res) => {
                this.orderInformation = res.data;
                console.log(res.data);
            })
            .catch((error) => {
                console.log('Failed to fetch order data.');
            });
        },
  
        toggleRole() {
            console.log("change")
            this.role = this.role === 'Buyer' ? 'Seller' : 'Buyer';
            this.getOrders();
        },
  
        showSellerDetails(order) {
            this.SellerselectedOrder = order;
            this.SellershowDialog = true;
        },

        closeSellerDetails() {
            this.SellerselectedOrder = null;
            this.SellershowDialog = false;
        },

        showBuyerDetails(order) {
            this.BuyerselectedOrder = order;
            this.BuyershowDialog = true;
        },
  
        closeBuyerDetails() {
            this.BuyerselectedOrder = null;
            this.BuyershowDialog = false;
        },
        
        deletBuyer(order){
            //console.log(order)
            const deletBuyerorder = {};
            const orderID = order.order_id;
            deletBuyerorder.order_id = this.orderID;

            axios.post('http://localhost:3000/deletBuyerorder', deletBuyerorder)
            .then((res) => {
                console.log('Successful delete order_id.');
            })
            .catch((error) => {
                console.log('Error delete order_id.');
            });
        },

        deletSeller(order){
            //console.log(order)
            const deletSellerorder = {};
            const orderID = order.order_id;
            deletSellerorder.order_id = this.orderID;

            axios.post('http://localhost:3000/deletBuyerorder', deletSellerorder)
            .then((res) => {
                console.log('Successful delete order_id.');
            })
            .catch((error) => {
                console.log('Error delete order_id.');
            });
        },

        goToPage(pageNumber) {
            this.currentPage = pageNumber;
        },
        
    },
};
</script>
  
<style scoped>
.order-box {
    font-family: Arial, sans-serif;
    border: 1px solid #ccc;
    padding: 5px;
    margin-bottom: 20px;
    background-color: #FFFFFF;
}
  
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}

.left-section {
    flex: 1;
}

.center-section {
    flex: 1.5;
    text-align: left;
}

.right-section {
    flex: 1d;
}

.order-details {
    display: flex;
    justify-content: space-between;
}

.order-sellerdetails {
    display: flex;
}
  
.v-card-actions {
    display: flex;
    justify-content: flex-end;
}

.order-sellerdetails {
    display: flex;
    justify-content: space-between;
}

.left-sellersection {
    flex: 1;
}

.center-sellersection {
    flex: 1;
}

.right-sellersection {
    align-items: center;
    flex: 0;
}

.fixed-pagination {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
}

p {
    margin-top: 3px;
    margin-bottom: 3px;
}
</style>