import http from "../http-common";

class CartDataService {
  getByUser(userId: number): Promise<any> {
    return http.get(`/cart/${userId}`);
  }

  delete(userId: number, marketId: number, productId: number): Promise<any> {
    return http.delete(`/cart/${userId}/${marketId}/${productId}`);
  }
}
export default new CartDataService();
