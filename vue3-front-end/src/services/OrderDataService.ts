import http from "../http-common";
import CreateOrder from "../models/order/create-order";

class OrderDataService {
  getByUser(userId: number): Promise<any> {
    return http.get(`/order/user/${userId}`);
  }

  getByMarket(marketId: number): Promise<any> {
    return http.get(`/order/market/${marketId}`);
  }

  create(data: CreateOrder): Promise<any> {
    return http.post("/order", data);
  }

  delete(orderId: number): Promise<any> {
    return http.delete(`/order/${orderId}`);
  }
}
export default new OrderDataService();
