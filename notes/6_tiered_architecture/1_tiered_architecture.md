# Tiered / Layered Architecture

Tiered architecture မှာ အဓိက layer သုံးခုရှိတယ်

- Presentation Layer
- Business Logic Layer
- Data Layer

## Presentation Layer

Presentation layer က end user တွေနဲ့တိုက်ရိုက်ထိတွေ့ရတဲ့ layer ဖြစ်တယ်။ Presentation layer မှာ data တွေကိုပြတယ် user ထည့်လိုက်တဲ့ input တွေကို capture လုပ်တယ်။
User ဆီကနေ input ကို request လုပ်တယ် ပြီးတောာ့ business logic layer ကို processing လုပ်ဖို့အတွက် pass ပေးတယ် ပြီးတော့ user ကိုပြန်ပြီး ပြပေးတယ်။

## Business Logic Layer

Business Logic Layer က application တစ်ခုလုံးရဲ့ heart ဖြစ်တယ်။ BLL မှာ core processing တွေ decision making တွေ Validation တွေလုပ်တယ်။

## Data Layer

Data Layer က application ရဲ့ data တွေကို သိမ်းတယ် manage လုပ်တယ်။ Database တွေနဲ့အလုပ်လုပ်တယ်။

## How three layer work together

User က presentation layer ကနေ interact လုပ်တယ်။ Presentation layer က user လုပ်လိုက်တဲ့ request ကို business logic layer ကိုပို့လိုက်တယ်။ Business Logic Layer က ရောက်လာတဲ့ request ကို ကြည့်ပြီး modify လုပ်မှာလား fetch လုပ်မှာလားဆုံးဖြတ်ပြီး data layer ကိုပို့တယ်။ Data processing တွေပြီးတဲ့အခါမှာ business logic layer က presentation layer ကိုပြန်ပို့တယ်။ Presentation layer က update လုပ်ပြီး user ကိုပြန်ပြပေးတယ်။

## Benefits

Scalability: layer တိုင်းက တစ်ခုနဲ့တစ်ခုမှီခိုမနေပဲ တစ်သီးတစ်ခြားစီလုပ်တဲ့အတွက် layer 3 ခု မှာ တစ်ခုကိုပြင်ရင် တစ်ခြားတစ်ခုကို affect မဖြစ်ဘူး။

Maintainability: သီးသန့်စီအလုပ်လုပ်တဲ့အတွက် update လုပ်ရတာလည်းလွယ်ကူတယ်။

Security: layer တွေခွဲထားတဲ့အတွက် security အရလည်းကောင်းတယ်။ Database ကို user တွေကို တိုက်ရိုက်ထိလို့မရဘူး 

Flexibility: အကယ်လို့ကိုယ်က presentation layer မှာသုံးထားတဲ့ framework ကိုမကြိုက်ဘူးဆိုရင် တစ်ခြားတစ်ခုကို အလွယ်တကူပြောင်းလို့ရတယ်။

---