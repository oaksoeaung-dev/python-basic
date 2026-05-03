Repository တစ်ခုကနေကိုယ့် စက်ထဲကို clone တော့မယ်ဆိုရင် python ရဲ့ module တွေက `.gitignore` ထဲမှာပါနေတဲ့အတွက် ပါမလာဘူး။ အဲ့တာကြောင့်ပြန် install လုပ်ပေးဖို့လိုအပ်ပါတယ်။

1. Create a virtual environment

    ```bash
    python -m venv venv
    ```
   
2. Activate the environment
   
   ```bash
   .\venv\Scripts\activate
   ```
   
3. Install the package

   `pip freeze > filename` နဲ့လုပ်ခဲ့တဲ့ file ထဲက package name တွေကိုသွင်းပေးရမယ်

   ```bash
   pip install -r .\packages.txt
   ```
   
4. Run the application from entry point