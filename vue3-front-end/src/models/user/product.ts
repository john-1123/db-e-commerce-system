// export default interface Product{
//     product_id: number;
//     product_name: string;
//     category: string;
//     brand: string;
//     price: number;
//     stock: number;
//     market_id: number;
//     status: boolean;
// }

export default class Product{
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
    status: boolean;
    product_id?: number;
    market_id?: number;

    constructor(
        product_name: string,
        category: string,
        brand: string,
        price: number,
        stock: number,
        status: boolean,
        product_id?: number,
        market_id?: number
    ){
        if(product_id) {
            this.product_id = product_id;
        }
        this.product_name = product_name;
        this.category = category;
        this.brand = brand;
        this.price = price;
        this.stock = stock;
        this.status = status;
        this.market_id = market_id;
    }
}

export interface UpdateProduct {
    product_id: number;
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
    market_id: number;
    status: boolean;
}

export interface CreateProduct {
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
}

export interface ChangeStatus {
    product_id: number;
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
    market_id: number;
    status: boolean;
}

export interface AddToCart {
    user_id: number;
    product_id: number;
    market_id: number;
    quantity: number;
}