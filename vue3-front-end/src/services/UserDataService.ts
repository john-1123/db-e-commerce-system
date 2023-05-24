import http from "../http-common";
import UpdateUser from "../models/user/update-user";
import User from "../models/user/user";

class UserDataService {
  get(id: number): Promise<any> {
    const user = new User(
      "john",
      "john@gmail.com",
      "password",
      "road",
      "0912345678"
    );
    return new Promise<User>((resolve) => {
      resolve(user);
    });
    // return http.get(`/users/${id}`);
  }
  
  update(id: number, data: UpdateUser): Promise<any> {
    return http.put(`/users/${id}`, data);
  }

  delete(id: number): Promise<any> {
    return http.delete(`/users/${id}`);
  }
}
export default new UserDataService();
