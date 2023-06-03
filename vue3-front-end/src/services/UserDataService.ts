import http from "../http-common";
import UpdateUser from "../models/user/update-user";

class UserDataService {
  get(id: number): Promise<any> {
    return http.get(`/users/${id}`);
  }

  update(id: number, data: UpdateUser): Promise<any> {
    return http.put(`/users/${id}`, data);
  }

  delete(id: number): Promise<any> {
    return http.delete(`/users/${id}`);
  }
}
export default new UserDataService();
