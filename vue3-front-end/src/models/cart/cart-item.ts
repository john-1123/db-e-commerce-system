import Product from "../product/product";

export default interface CartItem {
  product: Product;
  quantity: number;
}
