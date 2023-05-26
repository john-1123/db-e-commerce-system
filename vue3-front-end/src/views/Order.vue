<template>
    <v-container>
        <div class="header"> 
            <h1>Order List</h1>
            <v-btn @click="toggleRole" color="tan">{{ role }}</v-btn>
        </div>
        <div v-if="role === 'Buyer'">
            <div v-for="order in orderInformation" :key="order.order_id">
                <div class="order-box">
                    <div class="order-details">
                        <div class="left-section">
                            <p>Product: {{ order.product_name }}</p>
                            <p>Price: {{ order.total_pay }} </p>
                        </div>
                        <div class="center-section">
                            <p>Market: {{ order.market_name }} </p>
                            <p>State: {{ order.state }}</p> 
                        </div>
                        <div class="right-section">
                            <v-btn @click="showBuyerDetails(order)" color="tan">
                                details
                            </v-btn>
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
                        <p>payment_method: {{ BuyerselectedOrder && BuyerselectedOrder.payment_method }}</p>
                        <p>shipping_address: {{ BuyerselectedOrder && BuyerselectedOrder.shipping_address }}</p>
                        <p>create_time: {{ BuyerselectedOrder && BuyerselectedOrder.create_time }}</p>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="tan" text @click="closeBuyerDetails">Close</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
        <div v-else>
            <div v-for="order in orderInformation" :key="order.order_id">
                <div class="order-box">
                    <div class="order-sellerdetails">
                        <div class="left-sellersection">
                            <p>Consignee Information</p>
                            <p>Consignee: {{ order.consignee }}</p>
                            <p>Shipping Address: {{ order.shipping_address }}</p>
                            <p>Phone Number: {{ }}</p>
                        </div>
                        <div class="center-sellersection">
                            <p>Product Information</p>
                            <p>Product: {{ }}</p>
                            <p>Price: {{ }}</p>
                        </div>
                        <div class="right-sellersection">
                            <v-btn @click="showSellerDetails(order)" color="tan" small>
                                Details
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
                    <p>create_time: {{ SellerselectedOrder && SellerselectedOrder.create_time }}</p>
                    <p>Last Modified Time: {{ SSellerselectedOrder && SellerselectedOrder.Last_modified_time }}</p>
                    <p>Shipping Address: {{ SellerselectedOrder &&  SellerselectedOrder.shipping_address }}</p>
                    <p>Payment Method: {{ SellerselectedOrder && SellerselectedOrder.payment_method }}</p>
                    <p>Mode of Transport: {{ SellerselectedOrder && SellerselectedOrder.mode_of_transport }}</p>
                </v-card-text>
                <v-card-actions>
                    <v-btn color="tan" text @click="closeSellerDetails">Close</v-btn>
                    <div v-if="SellershowDialog"></div>
                </v-card-actions>
            </v-card>
        </v-dialog>
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
        };
    },
  
    mounted() {
        this.getOrders();
    },
  
    methods: {
        getOrders() {
            const apiUrl = this.role === 'Buyer' ? 'http://localhost:3000/order_buyer' : 'http://localhost:3000/order_seller';
            axios
            .get(apiUrl)
            .then((res) => {
                this.orderInformation = res.data;
            })
            .catch((error) => {
                console.log('Failed to fetch order data.');
            });
        },
  
        toggleRole() {
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
    },
};
</script>
  
<style scoped>
.order-box {
    font-family: Arial, sans-serif;
    border: 10px solid #ccc;
    padding: 5px;
    margin-bottom: 20px;
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
    flex: 1;
    text-align: left;
}

.right-section {
    flex: 0;
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
</style>