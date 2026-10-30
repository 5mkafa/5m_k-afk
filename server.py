from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# قائمة المفاتيح الـ 50 المكونة من أحرف وأرقام مع مفتاح المالك الخاص بك
VALID_KEYS = {
    "5mk-owner-0001": None,
    "5mk-A482-9B04": None,
    "5mk-37C6-18X9": None,
    "5mk-89D3-40F2": None,
    "5mk-1E48-5932": None,
    "5mk-72H1-38J5": None,
    "5mk-6K12-8930": None,
    "5mk-2L34-7M09": None,
    "5mk-9N60-23P4": None,
    "5mk-3Q05-6R82": None,
    "5mk-8S72-19T0": None,
    "5mk-5U01-48V3": None,
    "5mk-2W48-76X0": None,
    "5mk-6Y39-20Z1": None,
    "5mk-1A28-3B47": None,
    "5mk-7C02-5D18": None,
    "5mk-4E93-8F24": None,
    "5mk-6G58-1H73": None,
    "5mk-2J87-4K01": None,
    "5mk-8L64-3M29": None,
    "5mk-5N30-6P14": None,
    "5mk-3Q41-7R58": None,
    "5mk-7S25-1T93": None,
    "5mk-1U69-8V05": None,
    "5mk-6W10-4X92": None,
    "5mk-2Y04-5Z31": None,
    "5mk-9A82-3B67": None,
    "5mk-4C73-1D28": None,
    "5mk-8E19-6F50": None,
    "5mk-3G48-7H06": None,
    "5mk-7J51-2K39": None,
    "5mk-1L30-4M25": None,
    "5mk-5N02-9P73": None,
    "5mk-2Q94-3R81": None,
    "5mk-6S21-5T48": None,
    "5mk-4U08-8V72": None,
    "5mk-8W50-1X94": None,
    "5mk-1Y64-7Z09": None,
    "5mk-9A32-4B10": None,
    "5mk-3C19-6D47": None,
    "5mk-6E04-1F83": None,
    "5mk-2G91-7H60": None,
    "5mk-7J85-3K42": None,
    "5mk-5L39-8M14": None,
    "5mk-1N40-6P52": None,
    "5mk-8Q23-4R90": None,
    "5mk-3S09-5T71": None,
    "5mk-7U41-2V68": None,
    "5mk-4W90-9X25": None,
    "5mk-6Y12-3Z90": None,
}

class LicenseRequest(BaseModel):
    key: str
    mwic: str

@app.post("/verify")
def verify_license(data: LicenseRequest):
    if data.key not in VALID_KEYS:
        raise HTTPException(status_code=400, detail="مفتاح التفعيل غير صحيح!")
    
    current_mwic = VALID_KEYS[data.key]
    
    if current_mwic is None:
        VALID_KEYS[data.key] = data.mwic
        return {"status": "success", "message": "تم ربط وتفعيل المفتاح بنجاح!"}
    elif current_mwic == data.mwic:
        return {"status": "success", "message": "تم التحقق بنجاح!"}
    else:
        raise HTTPException(status_code=400, detail="المفتاح مستخدم على جهاز آخر!")
