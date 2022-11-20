from pydantic import BaseModel

class Driver(BaseModel):
    id: int	
    nama: str	
    plat_kendaraan: str	
    tipe_kendaraan: str	
    jumlah_pesanan: int	
    rating: float	
    jarak: float

    class Config:
        extra = {
            "example": {
                "id": 2,	
                "nama": "Cihuy",
                "plat_kendaraan": "D2345ADB",	
                "tipe_kendaraan": "Honda Beat",	
                "jumlah_pesanan": 23,	
                "rating": 4.5,	
                "jarak": 2.3
            }
        }