import http from "../http-common";

class CartDataService {
  getByUser(userId: number): Promise<any> {
    return http.get(`/cart/member/${userId}`);
  }
}
export default new CartDataService();
