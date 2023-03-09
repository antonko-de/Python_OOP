from project.product import Product

class ProductRepository:
    
    def __init__(self) -> None:
        self.products:list = []
        
    def add(self, product: Product) -> None:
        self.products.append(product)
        
    def find(self, product_name:str) -> Product:
        for prod in self.products:
            if prod.name == product_name:
                return prod
        
    
    def remove(self, product_name:str) -> None:
        prod = self.find(product_name=product_name)
        
        if prod:
            self.products.remove(prod)
        
    def __repr__(self) -> str:
        output = ''
        for prod in self.products:
            output += f"{prod.name}: {prod.quantity}\n"
            
        return output[:-1:]
            