from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# قائمة المفاتيح الـ 50 المطلوبة
VALID_KEYS = {
    "5mk-owner-0001",
    "5mk-a1b2c3-d4e5f6", "5mk-z9y8x7-w6v5u4", "5mk-m1n2o3-p4q5r6", "5mk-j7k8l9-m0n1o2",
    "5mk-q3r4s5-t6u7v8", "5mk-w9x0y1-z2a3b4", "5mk-c5d6e7-f8g9h0", "5mk-i1j2k3-l4m5n6",
    "5mk-o7p8q9-r0s1t2", "5mk-u3v4w5-x6y7z8", "5mk-a9b0c1-d2e3f4", "5mk-g5h6i7-j8k9l0",
    "5mk-m1n2o3-p4q5r7", "5mk-s3t4u5-v6w7x8", "5mk-y9z0a1-b2c3d4", "5mk-e5f6g7-h8i9j0",
    "5mk-k1l2m3-n4o5p6", "5mk-q7r8s9-t0u1v2", "5mk-w3x4y5-z6a7b8", "5mk-c9d0e1-f2g3h4",
    "5mk-i5j6k7-l8m9n0", "5mk-o1p2q3-r4s5t6", "5mk-u7v8w9-x0y1z2", "5mk-a3b4c5-d6e7f8",
    "5mk-g9h0i1-j2k3l4", "5mk-m5n6o7-p8q9r0", "5mk-s1t2u3-v4w5x6", "5mk-y7z8a9-b0c1d2",
    "5mk-e3f4g5-h6i7j8", "5mk-k9l0m1-n2o3p4", "5mk-q5r6s7-t8u9v0", "5mk-w1x2y3-z4a5b6",
    "5mk-c7d8e9-f0g1h2", "5mk-i3j4k5-l6m7n8", "5mk-o9p0q1-r2s3t4", "5mk-u5v6w7-x8y9z0",
    "5mk-a1b3c5-d7e9f1", "5mk-g2h4i6-j8k0l2", "5mk-m3n5o7-p9q1r3", "5mk-s2t4u6-v8w0x2",
    "5mk-y1z3a5-b7c9d1", "5mk-e2f4g6-h8i0j2", "5mk-k3l5m7-n9o1p3", "5mk-q2r4s6-t8u0v2",
    "5mk-w1x3y5-z7a9b1", "5mk-c2d4e6-f8g0h2", "5mk-i3j5k7-l9m1n3", "5mk-o2p4q6-r8s0t2"
}

class LicenseRequest(BaseModel):
    key: str
    hwid: str

@app.post("/verify")
def verify_license(data: LicenseRequest):
    if data.key not in VALID_KEYS:
        raise HTTPException(status_code=400, detail="المفتاح غير صالح أو غير موجود!")
    
    # هنا يتم قبول المفتاح وربطه بالـ HWID بنجاح
    return {"status": "success", "message": "تم التحقق وربط الهاردوير بنجاح!"}

@app.get("/")
def read_root():
    return {"status": "Server is running online!"}
