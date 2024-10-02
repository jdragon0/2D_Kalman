# 2D_Kalman
xy평면에서 Random하게 움직이는 물체를 추적하는 모델을 설계하고 칼만필터로 Tracking하는 예제.

## 시스템 설계
xy평면에서 움직이는 물체를 인식하기위해 위치와 속도와 가속도를 변수로 선택했고
아래와 같이 시스템을 설계하였다.

```math



\begin{align}
X_k = AX_{k-1}+w\\
X_k=
\begin{bmatrix}
    x_k & y_k \\ \dot{x}_k&\dot{y}_k \\ \ddot{x}_k& \ddot{y}_k
\end{bmatrix}=
\begin{bmatrix}
    1 & \Delta t & \Delta t^2\over2 \\ 0 & 1 & \Delta t \\ 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
    x_{k-1} & y_{k-1} \\ \dot{x}_{k-1}&\dot{y}_{k-1} \\ \ddot{x}_{k-1}& \ddot{y}_{k-1}
\end{bmatrix}
\\

\\
A = 
\begin{bmatrix}
    1 & \Delta t & \Delta t^2\over2 \newline 0 & 1 & \Delta t \newline 0 & 0 & 0
\end{bmatrix}\\
\\
\\
\\
z_k=Hx_k+v \\
z_k=\begin{bmatrix}
    1&0&0
\end{bmatrix}
\begin{bmatrix}
    x_k & y_k \newline \dot{x}_k & \dot{y}_k \newline \ddot{x}_k & \ddot{y}_k
\end{bmatrix}
=
\begin{bmatrix}
    x_k & y_k
\end{bmatrix}
\\


\\
H=\begin{bmatrix}
    1&0&0
\end{bmatrix}
\\
\\
\\
Q = \begin{bmatrix}
    dt^4\over4 & dt^3\over2 & dt^2\over2 \\
    dt^4\over4 & dt^3\over2 & dt^2\over2 \\
    dt^4\over4 & dt^3\over2 & dt^2\over2 \\
\end{bmatrix}*q
\\
\\
\end{align}
```
q(Q)와 R은 실험적으로 적당한 값을 선택했다.

## 결과
### 같은 경로를 움직이는 물체를 각각 다른 samplerate로 관찰하며 각각 Kalman filter를 적용해 시뮬레이션함

### N = 100
![image](https://github.com/user-attachments/assets/b06b9a73-51b3-4701-9879-4f9257a4a060)

### N = 500
![image](https://github.com/user-attachments/assets/330399d5-504c-426c-a5fd-9a6f2834a23c)

### N = 1000
![image](https://github.com/user-attachments/assets/23ca5cc7-cb04-4d3e-8935-8ca5b2c363c7)



o : 관측 물체 위치

x : 추정 된 물체 위치

점선 : 실제 물체 이동 경로

노이즈가 큰 상황에서도 Samplerate가 높으면 실제 물체 위치를 성공적으로 추정할 확률이 높은것 같다. 근본적으로 잡음제거 알고리즘이므로 고주파 성분에 대해서는 정보손실이 생길수 있음에 주의해야한다.
