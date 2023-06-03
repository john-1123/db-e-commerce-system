export interface CreateProduct {
    product_name: string;
    category: string;
    brand: string;
    price: number;
    stock: number;
    status: boolean;
    market_id: number;
}