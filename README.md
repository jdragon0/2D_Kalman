# 2D_Kalman
xy평면에서 Random하게 움직이는 물체를 추적하는 모델을 설계하고 칼만필터로 Tracing하는 예제.

## 시스템 설계
```math

\begin{align}
X_k = AX_{k-1}+w\\
X_k=
\begin{bmatrix}
    x_k & y_k \\ \dot{x_k}&\dot{y_k} \\ \ddot{x_k}& \ddot{y_k}
\end{bmatrix}=
\begin{bmatrix}
    1 & \Delta t & \Delta t^2\over2 \\ 0 & 1 & \Delta t \\ 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
    x_{k-1} & y_{k-1} \\ \dot{x_{k-1}}&\dot{y_{k-1}} \\ \ddot{x_{k-1}}& \ddot{y_{k-1}}
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
    x_k & y_k \newline \dot{x_k} & \dot{y_k} \newline \ddot{x_k} & \ddot{y_k}
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
\\
\\
\end{align}
```
Q와 R은 실험적으로 만들어서 계산해 보았다.

# 결과

![image](https://github.com/user-attachments/assets/cac4e3f8-c90e-46c9-8bf4-4f9011e81d98)


o : 관측 물체 위치

x : 추정 된 물체 위치

점선 : 실제 물체 이동 경로
