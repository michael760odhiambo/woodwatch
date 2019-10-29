# from django import forms
# from .models import Notifications,Business,Profile,Post,Comment,Hoods,Joinhood

# class TrendingForm(forms.ModelForm):
#     class Meta:
#         model=Notifications
#         exclude=['author','hood','post_date','priority','author']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         exclude=['']

# class PostForm(forms.ModelForm):
#     class Meta:
#         model=Post
#         exclude=['username','hood','avatar']

# class BusinessForm(forms.ModelForm):
#     class Meta:
#         model=Business
#         exclude=['owner','hood']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model=Comment
#         exclude=['username','post']

# class HoodForm(forms.ModelForm):
#     class Meta:
#         model = Hoods
#         exclude = [''] 

# class JoinHoodForm(forms.ModelForm):
#     class Meta:
#         model = Joinhood
#         exclude = ['']                