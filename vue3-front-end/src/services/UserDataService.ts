import http from "../http-common";
import UpdateUser from "../models/user/update-user";


class UserDataService {
  // getAll(): Promise<any> {
  //   return http.get("/users");
  // }

  get(id: number): Promise<any> {
    return http.get(`/users/${id}`);
  }

  // create(data: CreateUser): Promise<any> {
  //   return http.post("/users", data);
  // }

  update(id: number, data: UpdateUser): Promise<any> {
    return http.put(`/users/${id}`, data);
  }

  delete(id: number): Promise<any> {
    return http.delete(`/users/${id}`);
  }

  // deleteAll(): Promise<any> {
  //   return http.delete(`/users`);
  // }
}
export default new UserDataService();
