# CLI Basic

> Current User

```pwsh
whoami
```

> Current Working Directory

```pwsh
pwd
```

> Change Directory

```pwsh
cd C:/Users/oakso/Documents
```

- Absolute path နဲ့ directory ပြောင်းတာဖြစ်တယ်။ Absolute path ဆိုတာက ကိုယ်သွားချင်တဲ့ directory path ကို အစကနေအဆုံးထိရိုက်ထည့်တာဖြစ်တယ်။

```pwsh
cd Documents
```

- Relative path နဲ့ directory ပြောင်းတာဖြစ်တယ်။ Relative path ဆိုတာ `pwd` ရိုက်လိုက်ရင်တွေ့ရမယ့် ကိုယ်လက်ရှိရောက်နေတဲ့ path ကနေပြီးတော့ ဆက်သွားတာဖြစ်တယ်။


> List

```pwsh
ls
```

- လက်ရှိရောက်နေတဲ့ directory အောက်မှာရှိတဲ့ folder တွေ file တွေကိုကြည့်တာဖြစ်တယ်။

> Clear Terminal

```pwsh
clear
```

```pwsh
cls
```

> Create a new folder

```pwsh
mkdir "New Folder"
```

```pwsh
mkdir NewFolder
```

- လက်ရှိရောက်နေတဲ့ directory ရဲ့ အောက်မှာ folder တစ်ခု create လုပ်တာဖြစ်တယ် folder name မှာ space ထဲချင်ရင် Double quote နှစ်ခုထဲမှာထည့်ရေးလို့ရပါတယ်။

> Create an empty file

```pwsh
echo "" > hello.txt
```

> Check active internet connection

```pwsh
ping google.com
```

> Install `winget`

```pwsh
Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
```

> Search avaliable package in winget

```pwsh
winget search [app_name]
```

> Installing package with `winget`

```pwsh
winget install [app_name]
```

> Uninstalling package with `winget`

```pwsh
winget uninstall [app_name]
```