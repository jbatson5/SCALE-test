.. _6-6A:

TSURFER Appendix A: Sensitivity/Uncertainty Notation
====================================================

In the following expressions, the notation E[X] represents the expected value of
random variable X, which is equal to the integral of X weighted by its
probability density function over the range of allowable values.

.. _6-6a-1:

Basic variables
---------------

I =

  number of integral response (experiment and applications) used in GLLS analysis

M 	=

  number of nuclear data parameters used in transport calculations (i.e., number of unique nuclide-reaction pairs multiplied by the number of energy groups)

**α** 	=

  M dimensional vector of prior nuclear data parameters, where component-i = α\ :sub:`i`

**A** 	=

  M by M diagonal matrix of prior nuclear data parameters, where diagonal element **A**\ (i,i) = α\ :sub:`i`

**m** 	=

  I dimensional vector of prior measured responses, where component-*i* = m\ :sub:`i`

**M** 	=

  I by I diagonal matrix of prior measured responses, where diagonal element **M**\ (i,i) = m\ :sub:`i`

**k(α)** 	=

  I dimensional vector of prior calculated responses obtained with nuclear data *α*, where component I = k\ :sub:`i`

**K** 	=

  I by I diagonal matrix of prior calculated responses, where diagonal element **K**\ (i,i) = k\ :sub:`i`

:math:`\mathbf{F}_{\mathbf{m} / \mathbf{k}}` =

  I by I diagonal matrix of “E/C” values =

  .. math::

    \begin{array}{l}
    \mathbf{M} \mathbf{K}^{-1}=\mathbf{K}^{-\mathbf{1}} \mathbf{M}
    \end{array}

  where diagonal element

  .. math::

    \mathrm{F}_{\mathrm{m} / \mathrm{k}}(\mathrm{i}, \mathrm{i})=\frac{\mathrm{m}_{\mathrm{i}}}{\mathrm{k}_{\mathrm{i}}}


:math:`{{\mathbf{\hat{F}}}_{\mathbf{m/k}}}` =

  I by I diagonal matrix, where diagonal element

  .. math::

    \mathrm{F}_{\mathrm{m} / \mathrm{k}}\left(\mathrm{i}, \mathrm{i}\right)=\frac{\mathrm{m}_{\mathrm{i}}}{\mathrm{k}_{\mathrm{i}}}

  for a relative-formatted response and :math:`\mathrm{F}_{\mathrm{m} / \mathrm{k}}(\mathrm{i}, \mathrm{i})=1`

**α′** 	=

  M dimensional vector of adjusted nuclear data parameters produced by GLLS procedure

**m′** 	=

  I dimensional vector of adjusted measured responses produced by GLLS procedure

**k′(α′)** 	=

  I dimensional vector of adjusted calculated responses obtained with modified  nuclear data **α′**

.. note:: **k′(α′) = m′**, due to GLLS adjustment procedure.  <<<<

:math:`\mathbf{\tilde{d}}\,` 	=

  original absolute discrepancy vector = :math:`\mathbf{k}-\mathbf{m}` , where component-i= :math:`{{k}_{i}}-{{m}_{i}}`

**d** 	=

  original relative discrepancy vector = :math:`\mathbf{K}^{-1}(\mathbf{k}-\mathbf{m})` , where component-i = :math:`\left(\mathrm{k}_{\mathrm{i}}-\mathrm{m}_{\mathrm{i}}\right) / \mathrm{k}_{\mathrm{i}}`

:math:`\mathbf{\hat{d}}`

  original mixed absolute-relative discrepancy vector, where component-i = :math:`\left(\mathrm{k}_{\mathrm{i}}-\mathrm{m}_{\mathrm{i}}\right) / \mathrm{k}_{\mathrm{i}}` for a relative-formatted response and :math:`\left(\mathrm{k}_{i}-\mathrm{m}_{\mathrm{i}}\right)` for an absolute-formatted response

:math:`[\boldsymbol{\Delta} \boldsymbol{\alpha}]` =

  M dimensional vector of relative variations in nuclear data = :math:`\mathbf{A}^{-1}\left(\boldsymbol{\alpha}^{\prime}-\boldsymbol{\alpha}\right)`
  where component-i = :math:`\frac{\alpha_{i}^{\prime}-\alpha_{i}}{\alpha_{i}}`

:math:`[\mathbf{\Delta m}]` =

  I dimensional vector of relative variations in measured responses = :math:`\mathbf{M}^{-1}\left(\mathbf{m}^{\prime}-\mathbf{m}\right)`
  where component-i = :math:`\frac{\text{m}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{m}}_{\text{i}}}}{{{\text{m}}_{\text{i}}}}\to \frac{\text{k}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{m}}_{\text{i}}}}{{{\text{m}}_{\text{i}}}}`

:math:`[\mathbf{\Delta m}]` =

  I dimensional vector of absolute variations in measured responses = :math:`\mathbf{m}^{\prime}-\mathbf{m}`
  where component-i :math:`\text{m}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{m}}_{\text{i}}}\to \text{k}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{m}}_{\text{i}}}`

:math:`[\mathbf{\Delta} \hat{\mathbf{m}}]` =

  I dimensional vector of mixed absolute-relative variations in measured responses, where component-i =
  :math:`\frac{\text{m}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{m}}_{\text{i}}}}{{{\text{m}}_{\text{i}}}}` for a relative-formatted response and
  :math:`\text{m}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{m}}_{\text{i}}}` for an absolute-formatted response

:math:`[\boldsymbol{\Delta} \mathbf{k}]` =

  I dimensional vector of relative variations in calculated responses =
  :math:`\mathbf{K}^{-1}\left(\mathbf{k}^{\prime}-\mathbf{k}\right)`
  where component-i = :math:`\frac{\text{k}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{k}}_{\text{i}}}}{{{\text{k}}_{\text{i}}}}`

:math:`[\boldsymbol{\Delta} \mathbf{k}]` =

  I dimensional vector of absolute variations in calculated responses = :math:`\mathbf{k'}-\mathbf{k}`, where component-i = :math:`\text{k}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{k}}_{\text{i}}}`

:math:`[\boldsymbol{\Delta} \hat{\mathbf{k}}]` =

  I dimensional vector of mixed absolute-relative variations in calculated responses, where component-i =
  :math:`\text{k}{{\text{ }\!\!'\!\!\text{ }}_{\text{i}}}-{{\text{k}}_{\text{i}}}` for an absolute formatted response

.. _6-6a-2:

Sensitivity Relations
---------------------

:math:`\widetilde{\mathbf{S}}_{\mathbf{k} \boldsymbol{\alpha}}` =

  I by M absolute sensitivity matrix; where element :math:`\widetilde{\mathbf{S}}_{\mathbf{k} \boldsymbol{\alpha}}(\mathrm{i}, \mathrm{n})=\alpha_{\mathrm{n}} \frac{\partial \mathrm{k}_{\mathrm{i}}}{\partial \alpha_{\mathrm{n}}}`

:math:`\mathbf{S}_{\mathbf{k} \boldsymbol{\alpha}}` =

  I by M relative sensitivity matrix = :math:`\mathbf{K}^{-1} \mathbf{S}_{\mathbf{k} \boldsymbol{\alpha}}`,
  where element :math:`\mathbf{S}_{k \alpha}(i, n)=\frac{\alpha_{n}}{k_{i}} \frac{\partial k_{i}}{\partial \alpha_{n}}`.

:math:`\hat{\mathbf{S}}_{\mathbf{k}\boldsymbol{\alpha}}` =

  I by M mixed absolute-relative sensitivity matrix, where element :math:`\hat{\mathbf{S}}_{\mathbf{k} \boldsymbol{\alpha}}(\mathrm{i}, \mathrm{n})=\frac{\alpha_{\mathrm{n}}}{\mathrm{k}_{\mathrm{i}}} \frac{\partial \mathrm{k}_{\mathrm{i}}}{\partial \alpha_{\mathrm{n}}}`
  if response-i is relative-formatted and :math:`\hat{\mathbf{S}}_{\mathbf{k} \boldsymbol{\alpha}}(\mathrm{i}, \mathrm{n})=\alpha_{\mathrm{n}} \frac{\partial \mathbf{k}_{\mathrm{i}}}{\partial \alpha_{\mathrm{n}}}` if response-i is absolute-formatted

.. math::

  \begin{array}{l}
  {[\boldsymbol{\Delta} \mathbf{k}]=\quad \mathbf{S}_{\mathbf{k} \boldsymbol{\alpha}}[\mathbf{\Delta} \boldsymbol{\alpha}]} \\
  {{[\boldsymbol{\Delta} \mathbf{k}}]=\mathbf{S}_{\mathbf{k} \boldsymbol{\alpha}}[\mathbf{\Delta} \boldsymbol{\alpha}]} \\
  {[\boldsymbol{\Delta} \hat{\mathbf{k}}]=\hat{\mathbf{S}}_{\mathbf{k} \boldsymbol{\alpha}}[\mathbf{\Delta} \boldsymbol{\alpha}]}
  \end{array}

.. _6-6a-3:

Absolute covariances
--------------------

:math:`{{\mathbf{\tilde{C}}}_{\mathbf{mm}}}` =

  I by I covariance matrix for prior measured experiment responses where element :math:`{{\mathbf{\tilde{C}}}_{\mathbf{mm}}}`\(i,j) =
  :math:`E\left( \delta {{m}_{i}}\,\delta {{m}_{j}} \right)`

:math:`{{\mathbf{\tilde{C}}}_{\mathbf{kk}}}` =

  I by I covariance matrix for prior calculated responses, where element :math:`{{\mathbf{\tilde{C}}}_{\mathbf{kk}}}`\ (i,j) =
  :math:`E\left( \delta {{k}_{i}}\,\delta {{k}_{j}} \right)`

:math:`{{\mathbf{\tilde{C}}}_{\mathbf{dd}}}` =

  I by I covariance matrix for the discrepancies (k-m), where element :math:`{{\mathbf{\tilde{C}}}_{\mathbf{dd}}}`\ (i,j) =
  :math:`E\left( \delta {{d}_{i}}\,\delta {{d}_{j}} \right)` = :math:`\mathrm{E}\left(\delta\left(\mathrm{k}_{\mathrm{i}}-\mathrm{m}_{\mathrm{i}}\right) \delta\left(\mathrm{k}_{\mathrm{j}}-\mathrm{m}_{\mathrm{j}}\right)\right)`

:math:`{{\mathbf{\tilde{C}}}_{\mathbf{k'k'}}}` =

  I by I covariance matrix for adjusted responses, where element :math:`{{\mathbf{\tilde{C}}}_{\mathbf{k'k'}}}`\(i,j) =
  :math:`E\left( \delta k{{'}_{i}}\,\delta k{{'}_{j}} \right)`

:math:`\boldsymbol{\sigma}_{\mathbf{m}}` =

  I by I diagonal matrix containing standard deviations in prior measured responses, where diagonal element
  :math:`\widetilde{\sigma}_{\mathrm{m}}\left(\mathrm{i} \mathrm{i}\right)=\sqrt{\widetilde{\mathrm{C}}_{\mathrm{mm}}(\mathrm{i}, \mathrm{i})}`

:math:`\boldsymbol{\sigma}_{\mathbf{k}}` =

  I by I diagonal matrix containing
  standard deviations in prior calculated responses, where diagonal element
  :math:`\widetilde{\sigma}_{\mathrm{k}}(\mathrm{i}, \mathrm{i})=\sqrt{\widetilde{\mathrm{C}}_{\mathrm{kk}}(\mathrm{i}, \mathrm{i})}`

:math:`\boldsymbol{\sigma}_{\mathbf{k}^{\prime}}`

.. _6-6a-4:

Relative covariances
--------------------

:math:`{{C}_{\mathbf{mm}}}` =

  I by I relative covariance matrix for prior measured responses, = :math:`\mathbf{M}^{-1}\left[\tilde{\mathbf{C}}_{\mathbf{m m}}\right] \mathbf{M}^{-1}`
  :math:`C_{m m}(i, j)=\frac{\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})}{\mathrm{m}_{\mathrm{i}} \mathrm{m}_{\mathrm{j}}}`

:math:`{{C}_{\boldsymbol{\alpha \alpha}}}` =

  M by M relative covariance matrix for prior nuclear data, where element
  :math:`\widetilde{C}_{\alpha \alpha}(i, j)`
  = :math:`\frac{\mathrm{E}\left(\delta \alpha_{\mathrm{i}} \delta \alpha_{\mathrm{j}}\right)}{\alpha_{\mathrm{i}} \alpha_{\mathrm{j}}}`

:math:`{{C}_{\mathbf{kk}}}` =

  I by I relative covariance matrix for prior calculated responses =
  :math:`\mathbf{K}^{-1}\left[\mathbf{C}_{\mathrm{kk}}\right] \mathbf{K}^{-1}`
  where element :math:`C_{k k}(i, j)=\frac{\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})}{\mathrm{k}_{\mathrm{i}} \mathrm{k}_{\mathrm{j}}}`

:math:`{{C}_{\mathbf{dd}}}`

  I by I relative covariance matrix for response discrepancies; =
  :math:`\mathbf{K}^{-1}\left[\mathbf{C}_{\mathbf{dd}}\right] \mathbf{K}^{-1}`,
  where element :math:`C_{d d}(i, j)=\frac{\mathrm{C}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j})}{\mathrm{k}_{\mathrm{i}} \mathrm{k}_{\mathrm{j}}}`

:math:`\boldsymbol{\sigma}_{\mathbf{m}}` =

  I by I diagonal matrix containing relative standard deviations in measured responses, where diagonal element
  :math:`\sigma_{\mathrm{m}}\left(\mathrm{i}, \mathrm{i}\right)=\sqrt{\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{i})}`

:math:`\boldsymbol{\sigma}_{\mathbf{k}}` =

  I by I diagonal matrix containing relative standard deviations in calculated responses, where diagonal element
  :math:`\sigma_{k^{\prime}}\left(\mathrm{i}, \mathrm{i}\right)=\sqrt{\mathrm{C}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i})}`

:math:`\boldsymbol{\sigma}_{\boldsymbol{\alpha}}` =

  M by M diagonal matrix containing standard deviations in nuclear data, where diagonal element
  :math:`\boldsymbol{\sigma}_{\boldsymbol{\alpha}}(\mathrm{i}, \mathfrak{i})=\sqrt{C_{\alpha \alpha}(i, i)}`

.. _6-6a-5:

Mixed absolute-relative covariances
-----------------------------------

If response-i and response-j are both absolute formatted, then

.. math::

  \begin{aligned}
  \hat{\mathrm{C}}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j}) &=\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j}) \\
  \hat{\mathrm{C}}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j}) &=\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j}) \\
  \hat{\mathrm{C}}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j}) &=\mathrm{C}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j}) \\
  \hat{\mathrm{C}}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j}) &=\mathrm{C}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})
  \end{aligned}

Likewise, if both response-i and response-j are relative-formatted, then

.. math::

  \begin{array}{l}
  \hat{\mathrm{C}}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})=\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})}{\mathrm{k}_{\mathrm{i}} \mathrm{k}_{\mathrm{j}}} \\
  \hat{\mathrm{C}}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})=\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})}{\mathrm{m}_{\mathrm{i}} \mathrm{m}_{\mathrm{j}}} \\
  \hat{\mathrm{C}}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j})=\mathrm{C}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j})}{\mathrm{d}_{\mathrm{i}} \mathrm{d}_{\mathrm{j}}} \\
  \hat{\mathrm{C}}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})=\mathrm{C}_{\mathrm{kk}^{\prime}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{kk}^{\prime}}(\mathrm{i}, \mathrm{j})}{\mathrm{k}_{\mathrm{i}}^{\prime} \mathrm{k}_{\mathrm{j}}^{\prime}}
  \end{array}

If response-i is absolute-formatted and response-j is relative-formatted, then

.. math::

  \begin{array}{l}
  \hat{\mathrm{C}}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})}{\mathrm{k}_{\mathrm{j}}} \\
  \hat{\mathrm{C}}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})}{\mathrm{m}_{\mathrm{j}}} \\
  \hat{\mathrm{C}}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{dd}}(\mathrm{i}, \mathrm{j})}{\mathrm{d}_{\mathrm{j}}}
  \hat{\mathrm{C}}_{\mathrm{k}^{\prime}\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})}{\mathrm{k}_{\mathrm{j}}^{\prime}}
  \end{array}

Similar expressions can be derived if response-i is relative-formatted, and
response-j is absolute-formatted.  The I by I diagonal matrices of standard
deviation values are the following:

.. math::

  \hat{\sigma}_{\mathrm{k}}(\mathrm{i}, \mathrm{i})=\left\{\begin{array}{ll}
  \sigma_{\mathrm{k}}(\mathrm{i}, \mathrm{i}) & \text { absolute-formatted } \\
  \sigma_{\mathrm{k}}(\mathrm{i}, \mathrm{i}) & \text { relative-formatted }
  \end{array}\right.

.. math::

  \hat{\sigma}_{\mathrm{m}}(\mathrm{i}, \mathrm{i})=\left\{\begin{array}{ll}
  \sigma_{\mathrm{m}}(\mathrm{i}, \mathrm{i}) & \text { absolute-formatted } \\
  \sigma_{\mathrm{m}}(\mathrm{i}, \mathrm{i}) & \text { relative-formatted }
  \end{array}\right.

.. math::

  \hat{\sigma}_{\mathrm{d}}(\mathrm{i}, \mathrm{i})=\left\{\begin{array}{ll}
  \sigma_{\mathrm{d}}(\mathrm{i}, \mathrm{i}) & \text { absolute-formatted } \\
  \sigma_{\mathrm{d}}(\mathrm{i}, \mathrm{i}) & \text { relative-formatted }
  \end{array}\right.

.. math::

  \hat{\sigma}_{\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i})=\left\{\begin{array}{ll}
  \sigma_{\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i}) & \text { absolute-formatted } \\
  \sigma_{\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i}) & \text { relative-formatted }
  \end{array}\right.

.. _6-6a-6:

Correlation matrices
--------------------

:math:`\mathbf{R}_{\mathbf{kk}}` =

  I by I correlation matrix for prior calculated responses, where element
  :math:`\mathrm{R}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})` =
  :math:`\frac{\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})}{\sigma_{\mathrm{k}}(\mathrm{i}, \mathrm{i}) \sigma_{\mathrm{k}}(\mathrm{j}, \mathrm{j})}=\frac{\mathrm{C}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})}{\sigma_{\mathrm{k}}(\mathrm{i}, \mathrm{i}) \sigma_{\mathrm{k}}(\mathrm{j}, \mathrm{j})}=\frac{\hat{\mathrm{C}}_{\mathrm{kk}}(\mathrm{i}, \mathrm{j})}{\hat{\sigma}_{\mathrm{k}}(\mathrm{i}, \mathrm{i}) \hat{\sigma}_{\mathrm{k}}(\mathrm{j}, \mathrm{j})}`


:math:`\mathbf{R}_{\mathbf{mm}}` =

  I by I correlation matrix for prior measured responses, where element
  :math:`\mathrm{R}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})`
  :math:`\frac{\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})}{\sigma_{\mathrm{m}}(\mathrm{i}, \mathrm{i}) \sigma_{\mathrm{m}}(\mathrm{j}, \mathrm{j})}=\frac{\mathrm{C}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})}{\sigma_{\mathrm{m}}(\mathrm{i}, \mathrm{i}) \sigma_{\mathrm{m}}(\mathrm{j}, \mathrm{j})}=\frac{\hat{\mathrm{C}}_{\mathrm{mm}}(\mathrm{i}, \mathrm{j})}{\hat{\sigma}_{\mathrm{m}}(\mathrm{i}, \mathrm{i}) \hat{\sigma}_{\mathrm{m}}(\mathrm{j}, \mathrm{j})}`

:math:`\mathbf{R}_{\boldsymbol{\alpha} \boldsymbol{\alpha}}` =

  M by M correlation matrix for prior nuclear data, where element
  :math:`\mathrm{R}_{\alpha \alpha}(\mathrm{i}, \mathrm{j})=\frac{\mathrm{C}_{\alpha \alpha}(\mathrm{i}, \mathrm{j})}{\sigma_{\alpha}(\mathrm{i}, \mathrm{i}) \sigma_{\alpha}(\mathrm{j}, \mathrm{j})}`

:math:`\mathbf{R}_{\mathbf{k}^{\prime} \mathbf{k}^{\prime}}` =

  I by I correlation matrix for adjusted responses, where element :math:`\mathrm{R}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}} \quad(\mathrm{i}, \quad \mathrm{j})`
  = :math:`\frac{C_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})}{\sigma_{\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i}) \sigma_{\mathrm{k}^{\prime}}(\mathrm{j}, \mathrm{j})}=\frac{\mathrm{C}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})}{\sigma_{\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i}) \sigma_{\mathrm{k}^{\prime}}(\mathrm{j}, \mathrm{j})}=\frac{\hat{\mathrm{C}}_{\mathrm{k}^{\prime} \mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{j})}{\hat{\sigma}_{\mathrm{k}^{\prime}}(\mathrm{i}, \mathrm{i}) \hat{\sigma}_{\mathrm{k}^{\prime}}(\mathrm{j}, \mathrm{j})}`










..
