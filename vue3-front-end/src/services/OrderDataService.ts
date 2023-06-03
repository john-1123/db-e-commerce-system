import http from "../http-common";
import CreateOrder from "../models/order/create-order";

class OrderDataService {
  create(data: CreateOrder): Promise<any> {
    return http.post(`/order`, data);
  }
}
export default new OrderDataService();
