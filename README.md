# FUNKY DOTFILES

```
    (\ /)
    ( . .)
    c(*)(*)
```

The files are managed using gnu stow, more info here: https://www.youtube.com/watch?v=y6XCebnB9gs&t=370s

## ZSH setup

autosuggesions plugin

`git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions`

zsh-syntax-highlighting plugin

`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting`

zsh-autocomplete plugin

`git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete`

## SDDM theme

Requires the following packages:

`sudo pacman -S qt5-quickcontrols qt5-quickcontrols2 qt5-graphicaleffects`

Edit /usr/lib/sddm/sddm.conf.d/default.conf 

`[Theme]
Current=sugar-candy`
