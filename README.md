# Brain tumor classification and segmentation, ENGS 106 final project
## UNet
Trained for 20 epochs with 32 batch size. Used the dice coeffecient and dice loss to determine how much do the ground-truth and the predicted masks overlab. Training for more epochs is eventually going to lead to more accurate segmentation of the tumors.
<table>
  <tr>
    <td align="center">
      <img src="results/UNetaccuracy.png" width="450"><br>
      <em>Accuracy over Epochs</em>
    </td>
    <td align="center">
      <img src="results/UNet loss.png" width="450"><br>
      <em>Dice Coeffecient Loss over Epochs</em>
    </td>
  </tr>
</table>
<div align="center">
  <img src="results/Segmentation 1.png" width="100%">
  <p><em>True vs Mask 1</em></p>
  
  <img src="results/Segmentation 2.png" width="100%">
  <p><em>True vs Mask 2</em></p>

 <img src="results/Segmentation 3.png" width="100%">
  <p><em>True vs Mask 3</em></p>

  <img src="results/Segmentation 4.png" width="100%">
  <p><em>True vs Mask 4</em></p>
</div>
## Link to the trained UNet Model:
<div align="center>
  <p><em><a href="[url](https://drive.google.com/drive/folders/1tLgqE4yXmmK_8laLebRbEMb98bWcG6A-?usp=drive_link)">UNet Model</a></em></p>
</div>
