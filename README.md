# Brain tumor classification and segmentation, ENGS 106 final project
## UNet
Trained for 20 epochs with 32 batch size. Used the dice coeffecient and dice loss to determine how much do the ground-truth and the predicted masks overlab. Training for more epochs is eventually going to lead to more accurate segmentation of the tumors.
<table>
  <tr>
    <td align="center">
      <img src="results/UNetaccuracy.png" width="450"><br>
      <em>Caption for Image 1</em>
    </td>
    <td align="center">
      <img src="results/UNet loss.png" width="450"><br>
      <em>Caption for Image 2</em>
    </td>
  </tr>
</table>
