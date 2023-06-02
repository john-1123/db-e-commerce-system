export default interface Product{
    product_id: number;
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
    market_id: number;
    status: boolean;
}

export interface UpdateProduct {
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
    status: boolean;
}

export interface CreateProduct {
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
}

export interface AddToCart {
    user_id: number;
    product_id: number;
    market_id: number;
    quantity: number;
}