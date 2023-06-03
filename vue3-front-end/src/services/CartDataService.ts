import http from "../http-common";
import QueryCart from "../models/cart/query-cart";

class CartDataService {
  getByMember(data: QueryCart): Promise<any> {
    return http.get("");
  }
}
export default new CartDataService();
