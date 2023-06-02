import http from "../http-common";
import Product from "../models/user/product";
import { UpdateProduct, CreateProduct, ChangeStatus} from "../models/user/product";
import AddtoCart from "../models/user/add-product-cart";
class ProductDataService {
    getAll(){
        const productList: Product[] = [
            new Product(
                "iPhone 14 Pro Max",
                "3C",
                "Apple",
                42400,
                5,
                true,
                7,
                7  
            ),
            new Product(
                "iPhone 13",
                "3C",
                "Apple",
                22400,
                10,
                false,
                5,
                5   
            ),
            new Product(
                "這世界很煩，但你要很可愛2： 願我們歷經善惡，依舊少女無畏！",
                "BOOK",
                "幸福文化",
                388,
                38,
                false,
                8,
                8   
            ),
            new Product(
                "渣男排行榜",
                "BOOK",
                "時報出版",
                277,
                9,
                true,
                9,
                9   
            ),
            new Product(
                "多功能電烤盤-經典款(內含平盤、章魚燒盤）",
                "Kitchen & Dining",
                "BRUNO",
                3480,
                1,
                false,
                4,
                4   
            )
        ];
        return new Promise<any>((resolve) => {
            resolve(productList);
        });
        // return http.get('/product/${id}');
    }


    get(id: number): Promise<Product[]>{
        const product: Product = 
            new Product(
                "iPhone 14 Pro Max",
                "3C",
                "Apple",
                42400,
                5,
                true,
                2,
                2   
            );
        return new Promise<any>((resolve) => {
            resolve(product);
        });
        // return http.get('/product/details/${id}');
    }

    create(data: CreateProduct){
        return http.post('/product', data);
    }

    update(id: number, data: UpdateProduct): Promise<any> {
        return http.put('/product/${id}', data);
    }

    delete(id: number): Promise<any> {
        return http.delete('/product/${id}');
    }
    
    ProductToCart(data: AddtoCart): Promise<any> {
        return http.post('/cart/product');
    }
    
}
export default new ProductDataService();