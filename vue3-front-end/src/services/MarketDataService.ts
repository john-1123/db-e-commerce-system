import http from "../http-common";

class MarketDataService {
  getAll() {
    return http.get("/markets/");
  }

  get(makretId: number) {
    return http.get(`/markets/${makretId}`);
  }

  getMarketByUser(userId: number) {
    return http.get(`/markets/user/${userId}`);
  }

  //   create(data: CreateProduct) {
  //     return http.post("/markets", data);
  //   }

  //   update(id: number, data: UpdateProduct): Promise<any> {
  //     return http.put(`/markets/${id}`, data);
  //   }

  delete(makretId: number): Promise<any> {
    return http.delete(`/markets/${makretId}`);
  }
}
export default new MarketDataService();
